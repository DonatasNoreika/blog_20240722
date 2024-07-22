from django.db import models
from django.contrib.auth.forms import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    content = models.TextField(verbose_name="Content", max_length=2000)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Author", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.author})"

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Post", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Content", max_length=1000)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Author", on_delete=models.CASCADE)
