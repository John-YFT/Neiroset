# Generated by Django 4.1.7 on 2023-02-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_alter_bb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Images'),
        ),
    ]
