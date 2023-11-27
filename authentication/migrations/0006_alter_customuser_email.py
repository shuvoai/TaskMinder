# Generated by Django 4.1.3 on 2022-12-07 07:32

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[authentication.validators.validate_aamarpay_email], verbose_name='email address'),
        ),
    ]