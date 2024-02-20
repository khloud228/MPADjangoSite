from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="authors",
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    text = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    fixed = models.BooleanField(default=False, verbose_name="Закреплён")
    published = models.BooleanField(default=True, verbose_name="Опубликован")

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class Image(models.Model):
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        verbose_name="Публикация",
        related_name="images",
    )
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return f"Изображение к {self.post}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
