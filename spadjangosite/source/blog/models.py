from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.models import Tag
from taggit.managers import TaggableManager, TaggedItem

from .services import slugify as ru_slugify


class RuTag(Tag):
    """
    Тэги сохраняющие оттранслитерированные кириличные тэги
    """
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        return ru_slugify(self.name)[:128]

class RuTaggedItem(TaggedItem):
    """
    хз чё
    """
    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return RuTag


class Post(models.Model):
    image = models.ImageField(
        upload_to='%Y/%m/%d/',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    slug = models.SlugField()
    text = RichTextUploadingField(verbose_name='Содержимое')
    description = RichTextUploadingField(verbose_name='Описание')
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор'
    )
    tags = TaggableManager(through=RuTaggedItem)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Метод сохранения экземпляра
        """
        if not self.slug:
            self.slug = ru_slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name = 'Публикации'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = RichTextUploadingField()
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    def __str__(self):
        return f'Комментарий от {self.post} к {self.author}'
