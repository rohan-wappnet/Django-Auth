# Generated by Django 4.1.4 on 2022-12-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_registration_email_remove_registration_fntxt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
