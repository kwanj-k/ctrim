# Generated by Django 2.1.9 on 2020-02-14 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200214_0851'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('stock', 'name')},
        ),
    ]
