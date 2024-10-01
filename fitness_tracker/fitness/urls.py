from django.urls import path
from .views import UserRegisterView, ActivityViewSet, NotificationViewSet, UserProgressView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
] + router.urls

urlpatterns += [
    path('progress/', UserProgressView.as_view(), name='user-progress'),
]
