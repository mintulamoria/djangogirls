from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#class Category(models.Model):
#    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
#    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
#    title = models.CharField(max_length=255, verbose_name="Title")

#    class Meta:
#        verbose_name = "Category"
#        verbose_name_plural = "Categories"
#        ordering = ['title']

#    def __str__(self):
#        return self.title
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
#    slug = models.SlugField(unique=True, null=False)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#    class Meta:
#       verbose_name = "Post"
#        verbose_name_plural = "Posts"
#        ordering = ['created_at']

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

def approved_comments(self):
    return self.comments.filter(approved_comment=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text