# Generated by Django 4.2 on 2023-06-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]
