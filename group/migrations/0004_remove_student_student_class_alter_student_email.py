# Generated by Django 5.1.2 on 2025-02-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
