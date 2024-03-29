# Generated by Django 4.2.9 on 2024-01-23 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Qualities",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sense_of_responsibility", models.IntegerField(null=True)),
                ("quality_of_work", models.IntegerField(null=True)),
                ("conceptual_design_ability", models.IntegerField(null=True)),
                ("problem_solving_ability", models.IntegerField(null=True)),
                ("technical_programming_skills", models.IntegerField(null=True)),
                ("takes_initiative", models.IntegerField(null=True)),
                ("team_work", models.IntegerField(null=True)),
                ("productivity", models.IntegerField(null=True)),
                ("independent_work", models.IntegerField(null=True)),
                ("honesty_integrity", models.IntegerField(null=True)),
                ("work_consistency", models.IntegerField(null=True)),
                ("capacity_for_change", models.IntegerField(null=True)),
                ("client_relations", models.IntegerField(null=True)),
                ("communication", models.IntegerField(null=True)),
                ("strategic_perspective", models.IntegerField(null=True)),
                ("punctuality_attendance", models.IntegerField(null=True)),
                ("professional_appearance", models.IntegerField(null=True)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
