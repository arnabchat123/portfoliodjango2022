# Generated by Django 3.2.9 on 2022-04-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='datestamp',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
