# Generated by Django 4.0.1 on 2022-02-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Is_active',
            field=models.BooleanField(default=True),
        ),
    ]