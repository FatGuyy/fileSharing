# Generated by Django 4.2.5 on 2023-09-16 11:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file_name', models.TextField()),
                ('uploader_name', models.TextField()),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
