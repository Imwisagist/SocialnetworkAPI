from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

LIMIT_CHARS = 50


class Group(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа',
        related_name='posts', blank=True, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации', related_name='posts'
    )
    image = models.ImageField(
        verbose_name='Изображение', upload_to='posts/', null=True, blank=True
    )

    def __str__(self):
        return self.text[:LIMIT_CHARS]

    class Meta:
        ordering = ('pub_date',)


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор комментария', related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Пост комментария', related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария',)
    created = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Подписчик', related_name='user'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор', related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_fields'
            )
        ]
