# Generated by Django 2.2.1 on 2019-06-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0002_auto_20190612_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualanmodel',
            name='tahun_transaksi',
            field=models.CharField(max_length=200),
        ),
    ]
