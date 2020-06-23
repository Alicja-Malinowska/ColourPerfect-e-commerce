# Generated by Django 3.0.6 on 2020-06-23 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200619_1059'),
        ('basket', '0003_auto_20200621_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='colour',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Colour'),
        ),
    ]