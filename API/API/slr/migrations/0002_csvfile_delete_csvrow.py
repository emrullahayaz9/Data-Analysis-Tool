# Generated by Django 4.2.7 on 2024-03-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_files/')),
            ],
        ),
        migrations.DeleteModel(
            name='CSVRow',
        ),
    ]
