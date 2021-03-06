# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 17:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=40)),
                ('semester', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('department', models.CharField(choices=[('IT', 'IT'), ('ECE', 'ECE')], default='IT', max_length=3)),
                ('ltp', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(333)])),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('skills', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('knowledge', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('interactivity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_codes', to='SabKuch.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('enrollment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('semester', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('department', models.CharField(choices=[('IT', 'IT'), ('ECE', 'ECE')], default='IT', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('fac_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('ECE', 'ECE')], default='IT', max_length=3)),
                ('courses', models.ManyToManyField(related_name='course_teacher', to='SabKuch.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SabKuch.Student'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fac_codes', to='SabKuch.Teacher'),
        ),
    ]
