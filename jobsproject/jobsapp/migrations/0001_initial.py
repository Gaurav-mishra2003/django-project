# Generated by Django 4.2.2 on 2024-02-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hyd_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('eaddress', models.CharField(max_length=50)),
                ('esallary', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
