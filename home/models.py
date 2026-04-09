from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

from home.managers import ArticleManager
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(unique=True,blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ArticleManager()
    adminobjects = models.Manager()

    def __str__(self):
        return f'{self.slug} - {self.updated_date}'

    def save(self, *args, **kwargs):
        if not self.slug:                     # Only generate if slug is empty
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Check if slug already exists and make it unique
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def recover(self, *args, **kwargs):
        self.is_deleted = False
        self.save()