# Generated by Django 4.1.6 on 2023-04-11 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadfile",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="User",
                to="main.user",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
