from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key for every model!
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=False)
    body = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
