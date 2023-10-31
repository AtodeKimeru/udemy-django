from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('title', 'public', 'create_at', 'update_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'create_at'
    list_filter = ('public', 'create_at')
    list_per_page = 10


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)