from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,"DRAFT"),
    (1,"PUBLISH")
    )
class post(models.Model):
    objects = models.Manager() 
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    updated_on=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)

class Meta:
    ordering = ['-created_on']
def __str__(self):
    return self.title
