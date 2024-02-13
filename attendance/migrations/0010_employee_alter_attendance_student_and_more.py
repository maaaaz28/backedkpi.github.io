# Generated by Django 4.2.9 on 2024-02-06 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0009_attendance"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("employee_code", models.CharField(blank=True, max_length=250, null=True)),
                ("first_name", models.CharField(max_length=250)),
                (
                    "gender",
                    models.CharField(
                        blank=True, choices=[("Male", "Male"), ("Female", "Female")], max_length=100, null=True
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                ("contact", models.CharField(blank=True, max_length=250, null=True)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="attendance.course")),
            ],
        ),
        migrations.AlterField(
            model_name="attendance",
            name="student",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="attendance.employee"),
        ),
        migrations.AlterField(
            model_name="classstudent",
            name="student",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="attendance.employee"),
        ),
        migrations.DeleteModel(
            name="Student",
        ),
    ]