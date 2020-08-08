from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# from django.conf import settings
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, related_name='favorites', on_delete=models.CASCADE)
    likes = models.ManyToManyField('Category')
    others = models.CharField(
        max_length=400, default="separate with a comma i.e ',' ")

    def __str__(self):
        return self.user_profile


class Socials(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, related_name='socials', on_delete=models.CASCADE)
    social_name = models.CharField(max_length=200)
    profile_url = models.URLField()

    def __str__(self):
        return self.profile_url

    class Meta:
        verbose_name_plural = 'Socials'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post/pic/')

    def publish_post(self):
        self.date_published = timezone.now()
        # self.updated_on = timezone.now()
        self.published = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approve_comment=True)

    def comments_count(self):
        return self.comments.filter(approve_comment=True).count()

    # def popular_posts(self):
    #     return self.filter(published=True).order_by('-views')[:5]

    def related_posts(self):
        return self.categories.all_posts()

    def published_posts(self):
        return self.filter(published=True)

    def drafts(self):
        return self.filter(published=False)

    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={'pk': self.pk})

    # def get_update_url(self):
    #     return reverse("post_detail", kwargs={'pk': self.pk})

    # def get_remove_url(self):
    #     return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

    # def save(self, *args, **kwargs):
        # super(Post, self).save(*args, **kwargs)
        # self.instance.author = get_user(request)
        # self.published_date = timezone.now()
        # self.updated_on = timezone.now()
        # self.save()

        # return super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    post_for = models.ManyToManyField(Post, related_name='categories')
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def all_posts(self):
        return self.post_for.all()

    def __str__(self):
        return self.category_name


def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
