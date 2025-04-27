from django import forms
from .models import Bug, Project, User

# Define forms for the Bug, Project, Register, and User forms

class ProjectForm(forms.ModelForm):
    class Meta:
        # set the model and fields for the Project form
        model = Project
        fields = ['title', 'description', 'team_members']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter project description'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'team_members': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'onchange': 'this.blur();',  # Automatically save selection on change
            }),
        }

class RegisterForm(forms.ModelForm):
    # define the confirm password field
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        label="Confirm Password"
    )

    class Meta:
        # set the model and fields for the Register form
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }

        
class BugForm(forms.ModelForm):
    class Meta:
        # set the model and fields for the Bug form
        model = Bug
        fields = ['title', 'description', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter bug title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bug description'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
