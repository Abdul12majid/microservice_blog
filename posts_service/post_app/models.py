from django.db import models
import uuid
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
    	verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)
	bookmarks = models.IntegerField(default=0)
	categories = models.ForeignKey(Category, on_delete=models.CASCADE)
	is_published = models.BooleanField(default=True)