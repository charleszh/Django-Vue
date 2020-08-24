from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ExecuteStatus(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class TestCase(models.Model):
    name = models.CharField(max_length=50)
    abstract = models.CharField(max_length=200)
    # steps = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='NA')
    execute_status = models.ForeignKey(ExecuteStatus, on_delete=models.SET_DEFAULT, default=2)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
