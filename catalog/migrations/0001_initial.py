# Generated by Django 5.1 on 2024-09-19 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование категории', max_length=100, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование продукта', max_length=100, verbose_name='Наименование продукт')),
                ('description', models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание продукта')),
                ('photo', models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='catalog/products_photo', verbose_name='Превью')),
                ('price', models.IntegerField(help_text='Введите стоимость продукта', verbose_name='Цена')),
                ('created_at', models.DateField(blank=True, help_text='Укажите дату создания', null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(blank=True, help_text='Укажите дату последнего изменения', null=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, help_text='Выберите категорию продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('category', 'name'),
            },
        ),
    ]
