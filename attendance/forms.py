from backend_internal_app2.models import Qualities
from .models import CustomUser
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm

from django.contrib.auth import get_user_model

from attendance.models import CustomUser 
User=get_user_model

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Qualities
        exclude= [ 'sense_of_responsibility', 'quality_of_work' ,'conceptual_design_ability','problem_solving_ability','technical_programming_skills', 'takes_initiative' , 'team_work' , 'productivity', 'independent_work', 'honesty_integrity', 'work_consistency', 'capacity_for_change' , 'client_relations', 'communication' , 'strategic_perspective' , 'punctuality_attendance' , 'professional_appearance']
        
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class QualitiesForm(forms.ModelForm):
    class Meta:
        model = Qualities
        exclude = ['date_updated']
        # 'sense_of_responsibility', 'quality_of_work' ,'conceptual_design_ability','problem_solving_ability','technical_programming_skills', 'takes_initiative' , 'team_work' , 'productivity', 'independent_work', 'honesty_integrity', 'work_consistency', 'capacity_for_change' , 'client_relations', 'communication' , 'strategic_perspective' , 'punctuality_attendance' , 'professional_appearance'


class QForm(forms.ModelForm):
    class Meta:
        model = Qualities
        exclude = ['date_updated''sense_of_responsibility', 'quality_of_work' ,'conceptual_design_ability','problem_solving_ability','technical_programming_skills', 'takes_initiative' , 'team_work' , 'productivity', 'independent_work', 'honesty_integrity', 'work_consistency', 'capacity_for_change' , 'client_relations', 'communication' , 'strategic_perspective' , 'punctuality_attendance' , 'professional_appearance']