# Generated by Django 3.0.6 on 2020-06-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_brand_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='display_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]