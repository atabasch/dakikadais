# Generated by Django 2.1.1 on 2018-11-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_uye_tcno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uye',
            name='tcno',
            field=models.CharField(blank=True, default='', max_length=11, null=True, unique=True, verbose_name='TC Kimlik No'),
        ),
    ]
