# Generated by Django 5.1.6 on 2025-03-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0008_remove_products_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0, help_text='Вказувати суму в доларах', verbose_name='Ціна'),
        ),
    ]
