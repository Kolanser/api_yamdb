from django.urls import include, path
from rest_framework import routers
from api.views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    CommentViewSet,
    ReviewViewSet,
    SignUpView,
    UserViewSet,
    TokenObtainPairView
)

v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')
v1_router.register(r'categories', CategoryViewSet, basename='сategories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

jwt_patterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(jwt_patterns)),
    # path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    # path('v1/auth/token/', MyTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
]
