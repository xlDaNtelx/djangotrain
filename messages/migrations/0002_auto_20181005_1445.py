# Generated by Django 2.1.2 on 2018-10-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
