# Generated by Django 4.0.2 on 2022-03-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
