# Generated by Django 4.0.6 on 2022-08-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZumaApp', '0002_alter_index_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='images/digi.jpeg'),
        ),
    ]
