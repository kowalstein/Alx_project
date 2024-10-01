from rest_framework import generics
from rest_framework import permissions, viewsets
from rest_framework import filters
from rest_framework.response import Response
from .models import Activity, Notification
from .serializers import UserSerializer, ActivitySerializer, NotificationSerializer
from django.contrib.auth.models import User
from django.db.models import Sum

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['date', 'duration', 'calories_burned']
    ordering = ['date'] # Default ordering

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserProgressView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        total_distance = activities.aggregate(Sum('distance'))['distance__sum'] or 0
        total_calories = activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        total_duration = activities.aggregate(Sum('duration'))['duration__sum'] or 0

        return Response({
            'total_distance': total_distance,
            'total_calories': total_calories,
            'total_duration': total_duration,
        })
