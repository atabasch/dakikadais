# Generated by Django 2.1.1 on 2018-12-09 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0010_auto_20181209_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='istek',
            name='kategori',
        ),
    ]