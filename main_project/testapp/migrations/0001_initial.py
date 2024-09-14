# Generated by Django 4.2.2 on 2024-02-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='employee_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('enumber', models.BigIntegerField()),
                ('esallay', models.BigIntegerField()),
                ('eaddress', models.CharField(max_length=200)),
            ],
        ),
    ]
