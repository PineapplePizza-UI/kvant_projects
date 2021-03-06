# Generated by Django 3.0.5 on 2020-04-16 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvant_proj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kvantum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvantum', models.CharField(max_length=50, verbose_name='квантум')),
                ('description', models.CharField(max_length=250, verbose_name='описание квантума')),
                ('kvantum_logo', models.ImageField(upload_to='img', verbose_name='логотип квантума')),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО преподователя')),
                ('b_date', models.DateField(verbose_name='дата рождения преподователя')),
                ('kvantum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kvant_proj.Kvantum')),
            ],
        ),
        migrations.CreateModel(
            name='Kvantorianec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('b_date', models.DateField(verbose_name='дата рождения')),
                ('kvantum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kvant_proj.Kvantum')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kvant_proj.Master')),
            ],
        ),
        migrations.CreateModel(
            name='kvant_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, verbose_name='название проекта')),
                ('description', models.CharField(max_length=500, verbose_name='описание проекта')),
                ('img', models.ImageField(blank=True, upload_to='img', verbose_name='фотографии проекта')),
                ('Key_words', models.ManyToManyField(to='kvant_proj.Key_words')),
                ('Kvantum', models.ManyToManyField(to='kvant_proj.Kvantum')),
                ('kvantorianec', models.ManyToManyField(to='kvant_proj.Kvantorianec')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kvant_proj.Master')),
            ],
        ),
    ]
