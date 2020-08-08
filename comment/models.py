from django.db import models
from post.models import Post
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments',
        on_delete=models.CASCADE
        )
    author = models.CharField(max_length=200)
    visitor = models.CharField(max_length=300, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True
        )
    approve_comment = models.BooleanField(
        default=False
        )

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
