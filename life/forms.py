from django import forms
from newlife.users.models import User


class UserDashboardForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name","class_choices","university","profile_image")

    class_choice = User.UserClassesChoices.choices
