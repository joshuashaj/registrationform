# Generated by Django 5.1.1 on 2024-09-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
