# Generated by Django 4.1.4 on 2023-06-17 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_agent1_user_id_agent2_user_id_agent3_user_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent1",
            name="queue",
            field=models.CharField(
                choices=[("1", "inque"), ("2", "assigned"), ("3", "dispatched")],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="agent2",
            name="queue",
            field=models.CharField(
                choices=[("1", "inque"), ("2", "assigned"), ("3", "dispatched")],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="agent3",
            name="queue",
            field=models.CharField(
                choices=[("1", "inque"), ("2", "assigned"), ("3", "dispatched")],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="agent4",
            name="queue",
            field=models.CharField(
                choices=[("1", "inque"), ("2", "assigned"), ("3", "dispatched")],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="agent5",
            name="queue",
            field=models.CharField(
                choices=[("1", "inque"), ("2", "assigned"), ("3", "dispatched")],
                max_length=100,
            ),
        ),
    ]
