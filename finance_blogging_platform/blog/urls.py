from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'post', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('register', register),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]