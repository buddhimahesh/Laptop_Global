# Generated by Django 3.2.15 on 2022-09-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0006_auto_20220913_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='brand',
            field=models.TextField(choices=[('Apple', 'Apple'), ('HP', 'HP'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Dell', 'Dell'), ('Lenovo', 'Lenovo'), ('MSI', 'MSI'), ('Microsoft', 'Microsoft'), ('Razor', 'Razor'), ('Toshiba', 'Toshiba'), ('Google', 'Google'), ('Samsung', 'Samsung')], max_length=100),
        ),
    ]