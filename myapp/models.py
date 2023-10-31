from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, default='Title', verbose_name='Título')
    content = models.TextField(null=True, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Miniatura', upload_to='articles')
    public = models.BooleanField(default=False, verbose_name='¿Publicado?')
    create_at = models.DateTimeField('create_at')
    update_at = models.DateTimeField('update_at')

    def __str__(self):
        return f'{self.title} {self.public}'
    
    class Meta:
        ordering = ['-create_at']
    

class Category(models.Model):
    name = models.CharField(max_length=110, default='Category')
    description = models.CharField(max_length=250)
    create_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'