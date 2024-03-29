# Generated by Django 2.1.1 on 2018-11-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=255, verbose_name='Maaş Miktar Aralığı: Ör: 1500-3000')),
                ('slug', models.SlugField(max_length=255, verbose_name='Maaş Url Adı')),
            ],
            options={
                'verbose_name': 'Maaş',
                'verbose_name_plural': 'Maaşlar',
                'db_table': 'maaslar',
            },
        ),
    ]
