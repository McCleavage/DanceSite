# Generated by Django 4.2.3 on 2023-07-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0002_alter_style_category_alter_style_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='style',
            name='category',
            field=models.CharField(choices=[('STD', 'Standard'), ('LTN', 'Latin')], default='STD', max_length=3),
        ),
        migrations.AlterField(
            model_name='style',
            name='rating',
            field=models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], default='5', max_length=1),
        ),
    ]
