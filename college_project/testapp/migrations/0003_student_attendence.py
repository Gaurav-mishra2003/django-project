# Generated by Django 4.2.2 on 2024-02-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_senrollment_form_senrollment_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('attendence', models.CharField(max_length=2)),
                ('Date', models.DateField()),
            ],
        ),
    ]
