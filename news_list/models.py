from django.db import models


class NewsCategory(models.Model):
    title = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user_id = models.IntegerField()
    user_news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_news.title
