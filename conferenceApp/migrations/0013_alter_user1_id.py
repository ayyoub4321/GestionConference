# Generated by Django 5.1 on 2024-11-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferenceApp", "0012_user1_id_alter_user1_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user1",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
