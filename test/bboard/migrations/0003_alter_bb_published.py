# Generated by Django 4.1.7 on 2023-02-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_alter_bb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Опубликовано'),
        ),
    ]
