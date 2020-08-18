# Generated by Django 2.2.4 on 2020-08-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]