from .models import Category, Post, Location
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'slug',
                    'is_published',
                    'created_at')

    class Meta:
        verbose_name_plural = 'Категории'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')

    class Meta:
        verbose_name_plural = 'Местоположения'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'text',
                    'pub_date',
                    'author',
                    'location',
                    'category',
                    'is_published',
                    'created_at')

    class Meta:
        verbose_name_plural = 'Публикации'
