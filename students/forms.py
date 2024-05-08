from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['st_no', 'fname', 'lname', 'email', 'field_of_study', 'gpa']
        labels = {
            'st_no': 'Student Number',
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field Of Study',
            'gpa': 'G.P.A'
        }

        widgets = {
            'st_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }
