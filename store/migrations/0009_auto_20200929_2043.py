# Generated by Django 3.1.1 on 2020-09-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200929_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
