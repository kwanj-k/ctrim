# Generated by Django 2.1.9 on 2020-02-14 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stock.Stock'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('stock', 'name')},
        ),
    ]