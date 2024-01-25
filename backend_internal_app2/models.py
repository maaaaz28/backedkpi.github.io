from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Qualities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sense_of_responsibility = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    quality_of_work = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    conceptual_design_ability = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    problem_solving_ability = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    technical_programming_skills = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    takes_initiative = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    team_work = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    productivity = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    independent_work = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    honesty_integrity = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    work_consistency = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    capacity_for_change = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    client_relations = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    communication = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    strategic_perspective = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    punctuality_attendance = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    professional_appearance = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(4)])
    create_date = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
