# Generated by Django 3.2.4 on 2021-06-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата приказа')),
                ('number', models.CharField(max_length=20, verbose_name='Номер приказа')),
                ('title', models.CharField(max_length=150, verbose_name='Название приказа')),
                ('text', models.TextField(verbose_name='Текст приказа')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Приказ по кадрам',
                'verbose_name_plural': 'Приказы по кадрам',
                'ordering': ['-date'],
            },
        ),
    ]
