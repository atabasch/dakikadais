# Generated by Django 2.1.1 on 2018-11-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_kategori_meslek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sehir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaka', models.TextField(blank=True, default='', null=True, verbose_name='Plaka')),
                ('isim', models.CharField(max_length=255, verbose_name='Şehir Adı')),
            ],
            options={
                'verbose_name': 'Şehir',
                'verbose_name_plural': 'Şehirler',
                'db_table': 'sehirler',
            },
        ),
    ]