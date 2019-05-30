from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255, default="berita")
    slug = models.SlugField(blank=True, editable=False)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    waktu_update= models.DateTimeField(auto_now=True)
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
    def __str__(self):
        return "{}. {}".format(self.id, self.title)