# Generated by Django 4.1.3 on 2023-01-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0004_alter_goal_quarter_alter_goal_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='review_status',
            field=models.CharField(choices=[('ACC', 'Accepted'), ('Pen', 'Pending')], default='Pen', max_length=10, verbose_name='Goal Review Status'),
        ),
    ]
