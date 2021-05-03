# Generated by Django 3.1.7 on 2021-04-16 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0007_auto_20210413_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'TEACHERS',
                'db_table': 'TEACHERS',
            },
        ),
        migrations.RemoveField(
            model_name='stud_fee',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='stud_sub',
            name='name',
        ),
        migrations.AddField(
            model_name='stud_data',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_sub'),
        ),
        migrations.AlterField(
            model_name='stud_sub',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
