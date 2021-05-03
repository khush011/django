# Generated by Django 3.1.7 on 2021-04-08 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('roll_number', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Student_data',
                'db_table': 'student record',
            },
        ),
        migrations.CreateModel(
            name='Stud_Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Student_subject',
                'db_table': 'student subjects',
            },
        ),
        migrations.CreateModel(
            name='Stud_Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Games', models.CharField(blank=True, choices=[('Paintball', 'Paintball'), ('Baseball', 'Baseball'), ('Polo', 'Polo'), ('Golf', 'Golf')], max_length=100, null=True)),
                ('name', models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_data')),
            ],
            options={
                'verbose_name_plural': 'student games',
                'db_table': 'student games',
            },
        ),
        migrations.CreateModel(
            name='Stud_Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FEE', models.IntegerField(null=True)),
                ('name', models.ForeignKey(default='empty', on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_data')),
                ('subject', models.ForeignKey(default='DEFAULT', on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_sub')),
            ],
            options={
                'verbose_name_plural': 'student Fees',
                'db_table': 'student Fees',
            },
        ),
    ]
