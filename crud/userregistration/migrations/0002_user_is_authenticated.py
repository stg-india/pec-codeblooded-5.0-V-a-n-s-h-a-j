# Generated by Django 4.2.6 on 2023-10-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_authenticated',
            field=models.BooleanField(null=True),
        ),
    ]
