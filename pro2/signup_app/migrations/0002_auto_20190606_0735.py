# Generated by Django 2.2.1 on 2019-06-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_model',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
