# Generated by Django 3.0.3 on 2020-02-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('Mobile', models.IntegerField(max_length=12, verbose_name='Mobile Number')),
                ('Msg', models.TextField(max_length=400, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CV', models.FileField(max_length=400, upload_to=None, verbose_name='Resume')),
            ],
        ),
    ]
