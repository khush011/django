# Generated by Django 3.1.7 on 2021-04-08 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20210408_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_fee',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_data'),
        ),
        migrations.AlterField(
            model_name='stud_games',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.stud_data'),
        ),
    ]
