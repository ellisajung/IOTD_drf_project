from django.db import models
from users.models import User

# Create your models here.


class Hashtag(models.Model):
    content = models.CharField("태그 내용", max_length=32, unique=True)

    def __str__(self):
        return self.content


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_articles")
    title = models.CharField("제목", max_length=50)
    content = models.TextField("내용")
    image = models.ImageField("이미지", upload_to="%Y/%m/", blank=True)
    likes = models.ManyToManyField(User, related_name="like_articles", blank=True)
    tags = models.ManyToManyField(Hashtag, blank=True)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)

    def __str__(self):
        return self.title

    # 좋아요 개수
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField("내용", max_length=100)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)

    def __str__(self):
        return self.content
