# Generated by Django 2.1.2 on 2018-10-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0002_auto_20181005_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='description',
            field=models.IntegerField(),
        ),
    ]
