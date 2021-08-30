# Generated by Django 3.1.2 on 2021-08-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arsip', '0011_auto_20210817_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='surat_keputusan',
            name='kategori',
            field=models.CharField(blank=True, choices=[('UNUJA', 'UNUJA'), ('FAKULTAS', 'FAKULTAS'), ('LEMBAGA', 'LEMBAGA')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='surat_keputusan',
            name='tanggal_sah',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
