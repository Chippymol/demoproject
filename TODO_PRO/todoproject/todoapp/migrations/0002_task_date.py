# Generated by Django 4.2.1 on 2023-05-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-12-02'),
            preserve_default=False,
        ),
    ]
