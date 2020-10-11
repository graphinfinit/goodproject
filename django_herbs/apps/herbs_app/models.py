from django.db import models
from time import timezone
# Create your models here.
from django.contrib.auth.models import User

class Herb_article(models.Model):
    herb_name = models.CharField('Название статьи',max_length = 200)
    herb_text = models.TextField('Содержание статьи')
    date_updatese = models.DateTimeField('Дата публикации',auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    def __str__(self):
        return '%s' % (self.herb_name)
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    
    
    

class Comment(models.Model):
    article = models.ForeignKey(Herb_article, on_delete = models.CASCADE)
    author_name =  models.CharField('Имя автора',max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)
    date_updatese = models.DateTimeField('дата публикации комментария',auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return '%s %s' % (self.article, self.id)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    

    