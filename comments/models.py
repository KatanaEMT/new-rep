from django.db import models
from django.contrib.auth.models import User
from posts.models import Publication


class Comment(models.Model):
    comment_text = models.TextField()
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    publication = models.ForeignKey(
        to=Publication,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text[:10]

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"