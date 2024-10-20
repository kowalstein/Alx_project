from django.urls import path, include
from .views import UserRegisterView, ActivityViewSet, NotificationViewSet, UserProgressView, UserLoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('progress/', UserProgressView.as_view(), name='user-progress'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('api/', include(router.urls)),
]
