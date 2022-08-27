from rest_framework import viewsets, mixins, filters
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from reviews.models import Category, Genre, Title, Review
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    CategorySerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
    TitleWriteSerializer,
)


class CategoryGenreViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Кастомный класс для категорий и жанров."""
    # permission_classes = ()
    search_fields = ('name', 'slug',)


class CategoryViewSet(CategoryGenreViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CategoryGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    """Класс для модели Title"""
    review = Review.objects.all()
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    # search_fields = ('following__username',)
    search_fields = (
        'name',
        'year',
        'category__slug',
        # 'genre_slug',
    )
    # permission_classes = ()
    # pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'PUT',):
            return TitleWriteSerializer
        return TitleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pass
    # def get_queryset(self, *args, **kwargs):
    #     title_id = self.kwargs.get('title_id')
    #     return Review.objects.filter(title_id=title_id)

    # def perform_create(self, serializer):
    #     title_id = self.kwargs.get('title_id')
    #     title = get_object_or_404(Title, id=title_id)
    #     serializer.save(author=self.request.user, title_id=title)


class ReviewViewSet(viewsets.ModelViewSet):
    """Получение и изменение публикаций."""
    serializer_class = ReviewSerializer
    # pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        return Review.objects.filter(title_id=title_id)

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title_id=title)
