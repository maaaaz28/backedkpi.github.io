# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# from adminside.models import User
 

# class AdminCreationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_staff = True  # Allow access to the admin site
#         user.is_superuser = True
#         if commit:
#             user.save()
#         return user