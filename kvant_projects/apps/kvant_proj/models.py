from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Key_words(models.Model):
    key_word = models.CharField(max_length=200, verbose_name='ключевые слова')

    def __str__(self):
        return f"{self.key_word} ({self.id})"

class Kvantum(models.Model):
    kvantum = models.CharField(max_length=50, verbose_name='квантум')
    description = models.CharField(max_length=250, verbose_name='описание квантума')
    kvantum_logo = models.ImageField(upload_to="img", verbose_name='логотип квантума')

    def __str__(self):
        return f"{self.kvantum} ({self.id})"

class Master(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО преподователя')
    kvantum = models.ForeignKey(Kvantum, on_delete=models.PROTECT)
    b_date = models.DateField(verbose_name='дата рождения преподователя')

    def __str__(self):
        return f"{self.fio}, {self.kvantum} ({self.id})"

class Kvantorianec(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО')
    b_date = models.DateField(verbose_name='дата рождения')
    kvantum = models.ForeignKey(Kvantum, on_delete=models.PROTECT)
    master = models.ForeignKey(Master, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.kvantum}, {self.fio}, {self.master} ({self.id})"

class kvant_projects(models.Model):
    project_name = models.CharField(max_length=50, verbose_name='название проекта')
    Kvantum = models.ManyToManyField(Kvantum)
    Key_words = models.ManyToManyField(Key_words)
    kvantorianec = models.ManyToManyField(Kvantorianec)
    description = models.CharField(max_length=500, verbose_name='описание проекта')
    master = models.ForeignKey(Master, on_delete=models.PROTECT)
    img = models.ImageField(upload_to="img", verbose_name='фотографии проекта', blank=True)

    def __str__(self):
        return f"{self.project_name} ({self.id})"





