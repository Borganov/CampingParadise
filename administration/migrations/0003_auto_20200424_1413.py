# Generated by Django 3.0.3 on 2020-04-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_batiments_emplacements_piscine_zonecamping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbres',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batiments',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='emplacements',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='piscine',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='zonecamping',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
    ]
