# Generated by Django 3.2 on 2023-11-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartmentId', models.CharField(max_length=10)),
                ('DepartmentName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeId', models.CharField(max_length=10)),
                ('EmployeeName', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=30)),
                ('DateOfjoining', models.CharField(max_length=10)),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
    ]
