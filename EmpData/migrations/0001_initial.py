# Generated by Django 4.1.4 on 2022-12-27 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_position', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('date_hired', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deptname', to='EmpData.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='EmpData.position')),
            ],
        ),
    ]
