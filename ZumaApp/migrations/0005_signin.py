# Generated by Django 4.0.6 on 2022-08-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZumaApp', '0004_rename_username_signup_email_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]