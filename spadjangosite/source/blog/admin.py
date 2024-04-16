from django.contrib import admin
from django.db.models.signals import pre_save

from taggit.models import Tag
from taggit.admin import TagAdmin

from .models import Post
from .services import prepoplated_slug


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CustomTagAdmin(TagAdmin):
    pre_save.connect(prepoplated_slug, sender=Tag)


admin.site.unregister(Tag)
admin.site.register(Tag, CustomTagAdmin)
