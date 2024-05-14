from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=200, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    zip_code = forms.CharField(max_length=20, required=False)
    country = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=False)
    application_type = forms.ChoiceField(choices=[('undergraduate', 'Undergraduate'), ('graduate', 'Graduate')], required=True)
    program_of_interest = forms.CharField(max_length=100, required=True)
    academic_record = forms.FileField(required=False)
    personal_statement = forms.FileField(required=False)
    resume = forms.FileField(required=False)

    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'city',
            'state',
            'zip_code',
            'country',
            'date_of_birth',
            'gender',
            'application_type',
            'program_of_interest',
            'academic_record',
            'personal_statement',
            'resume',
        ]