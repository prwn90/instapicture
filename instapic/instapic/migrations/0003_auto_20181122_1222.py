# Generated by Django 2.1.3 on 2018-11-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapic', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilepic',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='sign_up_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
