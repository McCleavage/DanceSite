# Generated by Django 4.2.3 on 2023-07-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0005_style_height_style_width_alter_style_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='height',
        ),
        migrations.RemoveField(
            model_name='style',
            name='width',
        ),
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.ImageField(default='static/images/dance.png', upload_to='static/images/'),
        ),
    ]