# Generated by Django 2.1.7 on 2019-05-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190511_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Brunch', 'Brunch'), ('Dessert', 'Dessert')], max_length=20),
        ),
    ]
