# Generated by Django 3.0.3 on 2020-03-09 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0002_auto_20200310_0420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylibrary',
            old_name='products',
            new_name='books',
        ),
        migrations.RemoveField(
            model_name='mylibrary',
            name='total',
        ),
    ]
