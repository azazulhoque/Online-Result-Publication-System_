# Generated by Django 2.1.5 on 2020-02-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200225_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='semester',
            field=models.CharField(choices=[('4-2', '4th year 2nd semester'), ('4-1', '4th year 1st semester'), ('3-2', '3rd year 1st semester')], max_length=50),
        ),
    ]
