# Generated by Django 4.2.11 on 2024-03-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(verbose_name='содержание'),
        ),
    ]