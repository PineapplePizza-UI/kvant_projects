from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Key_words(models.Model):
    key_word = models.CharField(max_length=200, verbose_name='ключевые слова')

    def __str__(self):
        return f"{self.key_word} ({self.id})"

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


class Kvantum(models.Model):
    kvantum = models.CharField(max_length=50, verbose_name='квантум')
    description = models.CharField(max_length=10000, verbose_name='описание квантума')
    kvantum_logo = models.ImageField(upload_to="img", verbose_name='логотип квантума', blank=True)

    def __str__(self):
        return f"{self.kvantum} ({self.id})"

    class Meta:
        verbose_name = 'Квантум'
        verbose_name_plural = 'Квантумы'


class Master(models.Model):
    fio = models.CharField(max_length=75, verbose_name='ФИО преподователя')
    kvantum = models.ForeignKey(Kvantum, on_delete=models.PROTECT)
    b_date = models.DateField(verbose_name='дата рождения преподователя', blank=True)

    def __str__(self):
        return f"{self.fio}, {self.kvantum} ({self.id})"

    class Meta:
        verbose_name = 'Наставник'
        verbose_name_plural = 'Наставники'


class Kvantorianec(models.Model):
    fio = models.CharField(max_length=75, verbose_name='ФИО')
    b_date = models.DateField(verbose_name='дата рождения', blank=True)
    kvantum = models.ForeignKey(Kvantum, on_delete=models.PROTECT)
    master = models.ForeignKey(Master, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.kvantum.kvantum}, {self.fio}, {self.master.fio} ({self.id})"

    class Meta:
        verbose_name = 'Кванторианец'
        verbose_name_plural = 'Кванторианцы'


class Kvant_projects(models.Model):
    project_name = models.CharField(max_length=100, verbose_name='название проекта')
    Kvantum = models.ManyToManyField(Kvantum)
    Key_words = models.ManyToManyField(Key_words)
    kvantorianec = models.ManyToManyField(Kvantorianec)
    description = models.CharField(max_length=10000, verbose_name='описание проекта')
    low_description = models.CharField(max_length=5000, verbose_name='краткое описание проекта')
    master = models.ForeignKey(Master, on_delete=models.PROTECT)
    img = models.ImageField(upload_to="img", verbose_name='фотографии проекта', blank=True)

    def __str__(self):
        return f"{self.project_name} ({self.id})"

    class Meta:
        verbose_name = 'Проект кванторианцев'
        verbose_name_plural = 'Проекты кванторианцев'






