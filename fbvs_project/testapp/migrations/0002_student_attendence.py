# Generated by Django 4.2.2 on 2024-02-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=40)),
                ('Srollno', models.IntegerField()),
                ('Sattendence', models.CharField(max_length=1)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
