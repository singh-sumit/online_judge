# Generated by Django 5.0 on 2023-12-09 13:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('testcase_input', models.TextField()),
                ('testcase_output', models.TextField()),
            ],
            options={
                'db_table': 'problems',
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('problems', models.ManyToManyField(to='core.problem')),
            ],
            options={
                'db_table': 'challenges',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('solution', models.TextField()),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.problem')),
            ],
            options={
                'db_table': 'submissions',
            },
        ),
    ]