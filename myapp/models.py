from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, default='Title')
    content = models.TextField(null=True)
    image = models.ImageField(default='null')
    public = models.BooleanField(default=False)
    create_at = models.DateTimeField('create_at')
    update_at = models.DateTimeField('update_at')

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=110, default='Category')
    description = models.CharField(max_length=250)
    create_at = models.DateTimeField()