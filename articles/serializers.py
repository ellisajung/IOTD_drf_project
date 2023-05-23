from rest_framework import serializers
from articles.models import Article, Comment
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content", "tags")
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"
        
