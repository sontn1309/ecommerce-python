# Generated by Django 3.1.1 on 2020-09-20 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200920_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
