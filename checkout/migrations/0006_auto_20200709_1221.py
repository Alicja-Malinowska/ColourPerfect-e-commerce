# Generated by Django 3.0.6 on 2020-07-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200709_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=240),
        ),
    ]