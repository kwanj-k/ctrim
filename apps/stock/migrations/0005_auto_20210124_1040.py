# Generated by Django 2.2.9 on 2021-01-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20210116_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stocks', to='stores.Store'),
        ),
    ]