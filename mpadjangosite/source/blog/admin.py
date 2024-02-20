from django.contrib import admin
from .models import Post, Image


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "created_date",
        "last_modified",
        "fixed",
        "published",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
