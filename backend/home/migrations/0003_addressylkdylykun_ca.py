# Generated by Django 2.2.28 on 2022-11-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addressylkdylykun'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressylkdylykun',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
