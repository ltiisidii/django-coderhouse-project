# Generated by Django 4.0.4 on 2022-05-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_alter_questions_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]