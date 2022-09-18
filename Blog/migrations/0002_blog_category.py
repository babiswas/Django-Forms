# Generated by Django 2.2 on 2022-09-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('PROGRAMMING', 'Programming'), ('TRAVEL', 'Travelling'), ('PHOTOGRAPHY', 'Photography')], default='PROGRAMMING', max_length=100),
        ),
    ]
