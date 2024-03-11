from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="authors",
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d", blank=True, null=True, verbose_name="Изображение"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    descriptive = RichTextUploadingField(null=True, blank=True, verbose_name='Описание')
    text = RichTextUploadingField(null=True, blank=True, verbose_name="Содержимое")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    published = models.BooleanField(default=True, verbose_name="Опубликован")
    tag = TaggableManager()

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    # def get_tag_url(self):
    #     return reverse('blog:tag', kwargs={'slug': tag})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-created_date',)
