# Generated by Django 4.1.7 on 2023-03-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_alter_bb_image_rez'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='image_rez',
            field=models.ImageField(null=True, upload_to='', verbose_name='Images_rez'),
        ),
    ]