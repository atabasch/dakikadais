# Generated by Django 2.1.1 on 2018-11-21 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181122_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uye',
            name='eposta',
        ),
    ]
