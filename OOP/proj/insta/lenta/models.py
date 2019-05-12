from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from PIL import Image

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field=models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    likes = GenericRelation(Like)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.likes

    def __repr__(self):
        return self.likes

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    @property
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey('lenta.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    city = models.CharField(max_length=100,null=True, blank=True,)
    description = models.CharField(max_length=100,null=True, blank=True,)
    phone = models.IntegerField(default=0,null=True, blank=True,)


    def __str__(self):
        return f'{self.user.username} Profile'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)