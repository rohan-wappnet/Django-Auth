# Generated by Django 4.1.4 on 2022-12-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fntxt', models.CharField(default='', max_length=50)),
                ('lntxt', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('pincode', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
