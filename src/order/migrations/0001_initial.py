# Generated by Django 5.0.1 on 2024-02-28 12:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningTypeCanAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Категория(что можно добавить в уборку)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Можно добавить(категория)',
                'verbose_name_plural': 'Можно добавить(категории)',
            },
        ),
        migrations.CreateModel(
            name='CleaningTypeInclude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Категория(что входит в уборку)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Что входит в уборку(категория)',
                'verbose_name_plural': 'Что входит в уборку(категории)',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_body', models.TextField(max_length=1000, verbose_name='Отзыв')),
                ('feedback_rating', models.IntegerField(choices=[(1, 'Очень плохо'), (2, 'Плохо'), (3, 'Удовлетворительно'), (4, 'Хорошо'), (5, 'Восхитительно')], default='amazing', verbose_name='Рейтинг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='FurnitureCluttered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Степень заставленности мебелью')),
                ('description', models.CharField(max_length=2000, verbose_name='Справка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Степень заставленности мебелью',
                'verbose_name_plural': 'Степень заставленности мебелью',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Площадь помещения')),
                ('room_choices', models.CharField(choices=[('apart', 'Квартира'), ('office', 'Офис'), ('workshop', 'Производство/Мастерская'), ('house', 'Загородный дом'), ('yacht', 'Яхта')], default='apartment', verbose_name='Тип помещения')),
                ('cleaning_date', models.DateField(verbose_name='Дата уборки')),
                ('cleaning_time', models.TimeField(verbose_name='Время')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/orders/%Y/%m/%D/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'webp'])], verbose_name='Фото квартиры')),
                ('window_clean', models.BooleanField(default=False, verbose_name='Мыть ли окна?')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('comment', models.TextField(max_length=1000, verbose_name='Пожелания/комментарии')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cleaners_photo', models.ImageField(blank=True, null=True, upload_to='media/orders/cleaner/%Y/%m/%D/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'webp'])], verbose_name='Фото квартиры после уборки')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='PollutionDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Степень загрязнения')),
                ('description', models.CharField(max_length=2000, verbose_name='Справка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Степень загрязнения',
                'verbose_name_plural': 'Степень загрязнения',
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название акции')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание акции')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('promocode', models.TextField(blank=True, null=True, verbose_name='Промокод')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.CreateModel(
            name='ThingsCluttered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Степень заставленности вещами')),
                ('description', models.CharField(max_length=2000, verbose_name='Справка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Степень заставленности вещами',
                'verbose_name_plural': 'Степень заставленности вещами',
            },
        ),
        migrations.CreateModel(
            name='CleaningTypeCanAddList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='что можно добавить в уборку(список)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cleaning_type_can_add', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='can_add_list', to='order.cleaningtypecanadd', verbose_name='Категория(что можно добавить в уборку)')),
            ],
            options={
                'verbose_name': 'Можно добавить(список)',
                'verbose_name_plural': 'Можно добавить(списки)',
            },
        ),
        migrations.CreateModel(
            name='CleaningType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип уборки')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание уборки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена за кв.м')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('kitchen_can_add', models.ManyToManyField(to='order.cleaningtypecanadd')),
                ('kitchen_include', models.ManyToManyField(to='order.cleaningtypeinclude')),
            ],
            options={
                'verbose_name': 'Тип уборки',
                'verbose_name_plural': 'Типы уборки',
            },
        ),
        migrations.CreateModel(
            name='CleaningTypeIncludeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='что входит в уборку(список)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cleaning_type_include', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='include_list', to='order.cleaningtypeinclude', verbose_name='Категория(что входит в уборку)')),
            ],
            options={
                'verbose_name': 'Что входит в уборку(список)',
                'verbose_name_plural': 'Что входит в уборку(списки)',
            },
        ),
    ]
