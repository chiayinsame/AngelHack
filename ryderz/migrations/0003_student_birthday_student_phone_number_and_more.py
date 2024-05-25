# Generated by Django 4.2 on 2024-05-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ryderz', '0002_remove_student_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='preferred_sex',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tutor',
            name='sex',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
