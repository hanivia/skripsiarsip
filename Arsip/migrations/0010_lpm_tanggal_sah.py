# Generated by Django 3.1.2 on 2021-08-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arsip', '0009_lpm_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpm',
            name='tanggal_sah',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
