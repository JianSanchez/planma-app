# Generated by Django 5.1.3 on 2024-11-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_customactivity_status_alter_customtask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsemester',
            name='acad_year_end',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='customsemester',
            name='acad_year_start',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='customsemester',
            name='semester',
            field=models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester')], max_length=1),
        ),
        migrations.AlterField(
            model_name='customsemester',
            name='year_level',
            field=models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year')], max_length=1),
        ),
    ]
