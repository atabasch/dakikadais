# Generated by Django 2.1.1 on 2018-11-22 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='istek',
            name='uye',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
