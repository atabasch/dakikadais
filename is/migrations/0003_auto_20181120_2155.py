# Generated by Django 2.1.1 on 2018-11-20 18:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_zaman'),
        ('is', '0002_firma_uye'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ilan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=255, verbose_name='İlan Başlığı')),
                ('slug', models.SlugField(editable=False, max_length=255, null=True, verbose_name='İlan url adı')),
                ('tecrube', models.CharField(choices=[('F', 'Farketmez'), ('az', '1 yıldan az'), ('1-3', '1-3 yıl'), ('3-5', '3-5 yıl'), ('5-10', '5-10 yıl'), ('deneyimli', '10 yıldan fazla')], default='F', max_length=11, verbose_name='Deneyim')),
                ('cinsiyet', models.CharField(choices=[('F', 'Farketmez'), ('E', 'Erkek'), ('K', 'Kadın')], default='F', max_length=1, verbose_name='Cinsiyet')),
                ('yas_min', models.SmallIntegerField(default=18, verbose_name='Minimum Yaş')),
                ('yas_max', models.SmallIntegerField(default=45, verbose_name='Maximum Yaş')),
                ('ayrintilar', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='İş Tanıtım Yazısı')),
                ('c_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Eklenme Tarihi')),
                ('u_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('askerlik', models.ManyToManyField(to='system.Askerlik', verbose_name='Askerlik Durumu')),
                ('dil_konusma', models.ManyToManyField(blank=True, default=None, null=True, related_name='konusulan_diller', to='system.Dil', verbose_name='Konuşulabilen Diller')),
                ('dil_yazma', models.ManyToManyField(blank=True, default=None, null=True, related_name='yazilan_diller', to='system.Dil', verbose_name='Yazılıp, Okunabilen Diller')),
                ('egitim', models.ManyToManyField(to='system.Egitim', verbose_name='Eğitim Seviyesi')),
            ],
            options={
                'verbose_name': 'İlan',
                'verbose_name_plural': 'İlanlar',
                'db_table': 'ilanlar',
            },
        ),
        migrations.AddField(
            model_name='firma',
            name='c_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Eklenme Tarihi'),
        ),
        migrations.AddField(
            model_name='firma',
            name='u_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='firma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='is.Firma', verbose_name='Çalışılacak Firma'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='kategori',
            field=models.ManyToManyField(to='system.Kategori', verbose_name='İş Kategorisi'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='maas',
            field=models.ManyToManyField(to='system.Maas', verbose_name='Muhtemel Maaş'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='meslek',
            field=models.ManyToManyField(to='system.Meslek', verbose_name='Meslek'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='sehir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Sehir', verbose_name='Çalışılacak Şehir'),
        ),
        migrations.AddField(
            model_name='ilan',
            name='zaman',
            field=models.ManyToManyField(to='system.Zaman', verbose_name='İş Kategorisi'),
        ),
    ]
