# Generated by Django 4.1.1 on 2023-01-17 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0002_alter_soal_category_alter_soal_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.soal')),
            ],
        ),
    ]
