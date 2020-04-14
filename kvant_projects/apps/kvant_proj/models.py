from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Key_words(models.Model):
    key_word = models.CharField(max_length=200, verbose_name='ключевые слова')

    def __str__(self):
        return f"{self.key_word} ({self.id})"


 # class Post(models.Model):
 #
 #    author = models.ForeignKey('auth.User')
 #
 #    title = models.CharField(max_length=200)
 #
 #    text = RichTextUploadingField()
