# Generated by Django 3.1.7 on 2021-04-16 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_auto_20210416_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_data',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.teacher'),
        ),
    ]