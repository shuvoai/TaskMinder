# Generated by Django 4.1.3 on 2023-01-10 07:15

from django.db import migrations, models
import goal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0005_alter_goal_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='completion',
            field=models.IntegerField(default=0, validators=[goal.validators.validate_completion], verbose_name='Goal total completion on percentage'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='review',
            field=models.TextField(blank=True, null=True, verbose_name='Review under goal'),
        ),
    ]