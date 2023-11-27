# Generated by Django 4.1.3 on 2023-01-29 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0012_alter_departmentmember_designation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Team title')),
                ('description', models.TextField(verbose_name='Team description')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_teams', to='department.department')),
                ('team_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_teams', to='department.departmentmember')),
            ],
            options={
                'unique_together': {('department', 'title')},
            },
        ),
    ]
