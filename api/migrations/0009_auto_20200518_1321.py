# Generated by Django 2.1.7 on 2020-05-18 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200516_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queues', to='api.Restaurant'),
        ),
    ]
