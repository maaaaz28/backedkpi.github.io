# Generated by Django 4.2.9 on 2024-02-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0011_alter_course_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="date_added",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
