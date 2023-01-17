# Generated by Django 4.1.1 on 2023-01-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soal',
            name='category',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=20),
        ),
        migrations.AlterField(
            model_name='soal',
            name='course',
            field=models.CharField(choices=[('Java', 'Java'), ('HTML', 'HTML'), ('Kotlin', 'Kotlin'), ('PHP', 'PHP'), ('Android Studio', 'Android Studio')], max_length=20),
        ),
    ]
