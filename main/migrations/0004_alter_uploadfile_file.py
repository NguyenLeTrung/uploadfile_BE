# Generated by Django 4.1.6 on 2023-04-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_uploadfile_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(upload_to="upload"),
        ),
    ]