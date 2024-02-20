from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Qualities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sense_of_responsibility = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    quality_of_work = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    conceptual_design_ability = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    problem_solving_ability = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(4)])
    technical_programming_skills = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    takes_initiative = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    team_work = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(4)])
    productivity = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    independent_work = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(4)])
    honesty_integrity = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(4)])
    work_consistency = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    capacity_for_change = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    client_relations = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    communication = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    strategic_perspective = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    punctuality_attendance = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    professional_appearance = models.PositiveIntegerField(null=True, validators=[ MaxValueValidator(4)])
    create_date = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    @property
    def get_user_record(self):
        previous_qualities = Qualities.objects.filter(create_date__lt=self.create_date).order_by('-create_date').first()
        latest_qualities = Qualities.objects.filter(create_date__gte=self.create_date).order_by('create_date').first()

        record = {
            'previous_user': previous_qualities.user.username if previous_qualities else None,
            'latest_user': latest_qualities.user.username if latest_qualities else None,
        }

        return record