from rest_framework import serializers
from .models import BlogPost, Category, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        blog_post = BlogPost.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            blog_post.tags.add(tag)
        return blog_post
