# Generated by Django 4.2 on 2024-05-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ryderz', '0003_student_birthday_student_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='birthday',
            field=models.DateField(),
        ),
    ]