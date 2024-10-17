# Generated by Django 5.1.1 on 2024-10-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.TextField(verbose_name="Содержимое"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="count_of_views",
            field=models.IntegerField(default=0, verbose_name="Количество просмотров"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="publication_sign",
            field=models.BooleanField(default=True, verbose_name="Признак публикации"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Заголовок"),
        ),
    ]
