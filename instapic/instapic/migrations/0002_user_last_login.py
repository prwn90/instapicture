# Generated by Django 2.1.3 on 2018-11-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
