from rest_framework import viewsets, permissions
from .models import BlogPost, Category
from .serializers import BlogPostSerializer, CategorySerializer

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset =BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
