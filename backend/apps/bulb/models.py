from django.db import models
from django.conf import settings


class Tags(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    def __str__(self):
        return f'{self.title}'


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    
    description = models.CharField(max_length=150, null=True)
    html_content = models.TextField(max_length=5000)
    
    action_click = models.CharField(max_length=30, default='Подробнее')
    main_img_url = models.ImageField(upload_to='images/', blank=True)

    tags = models.ForeignKey(
        Tags, 
        null=True,
        on_delete = models.SET_NULL
        )
    publish_date = models.DateTimeField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
        default = 0,
        null = True,
        on_delete = models.SET_NULL
        )
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
    def __str__(self):
        return f'{self.title} от {self.publish_date}. Автор: {self.autor}'


class Comments(models.Model):
    news = models.ForeignKey(
        News, 
        null=True,
        on_delete = models.SET_NULL
        )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        default = 0,
        null = True,
        on_delete = models.SET_NULL
        )
    date = models.DateTimeField()
    content = models.CharField(max_length=500)
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return f'{self.content} от {self.user}. К записи: {self.news}'
