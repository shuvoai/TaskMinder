# Generated by Django 4.1.3 on 2023-01-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_alter_taskattachments_attached_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_assigned',
            field=models.BooleanField(default=False, verbose_name='Is task already assigned'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('NON', 'Type not yet fixed'), ('RGT', 'Regular task'), ('DPT', 'Department task'), ('PRT', 'Project task'), ('TMT', 'Team task')], default='NON', max_length=3, verbose_name='Task type'),
        ),
    ]
