# Generated by Django 2.1.1 on 2018-11-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_uye_eposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uye',
            name='telefon',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Telefon Numarası'),
        ),
    ]