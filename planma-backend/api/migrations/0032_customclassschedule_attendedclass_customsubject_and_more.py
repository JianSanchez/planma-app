# Generated by Django 5.1.3 on 2024-12-18 06:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_customclassschedule_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomClassSchedule',
            fields=[
                ('classsched_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=10)),
                ('scheduled_start_time', models.TimeField()),
                ('scheduled_end_time', models.TimeField()),
                ('room', models.CharField(max_length=75)),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_classes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttendedClass',
            fields=[
                ('att_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('isExcused', models.BooleanField(default=False)),
                ('hasAttended', models.BooleanField()),
                ('classched_id', models.ForeignKey(db_column='classsched_id', on_delete=django.db.models.deletion.CASCADE, related_name='attendedclass', to='api.customclassschedule')),
            ],
        ),
        migrations.CreateModel(
            name='CustomSubject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_title', models.CharField(max_length=255)),
                ('semester_id', models.ForeignKey(db_column='semester_id', on_delete=django.db.models.deletion.CASCADE, related_name='subsems', to='api.customsemester')),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('subject_code', 'student_id', 'semester_id')},
            },
        ),
        migrations.AddField(
            model_name='customclassschedule',
            name='subject',
            field=models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='api.customsubject'),
        ),
        migrations.CreateModel(
            name='CustomTask',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('task_desc', models.TextField()),
                ('scheduled_date', models.DateField()),
                ('scheduled_start_time', models.TimeField()),
                ('scheduled_end_time', models.TimeField()),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('subject_id', models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='api.customsubject')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customclassschedule',
            unique_together={('subject', 'day_of_week', 'scheduled_start_time', 'scheduled_end_time', 'room', 'student_id')},
        ),
    ]