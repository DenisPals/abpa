from django import forms
from .models import MembershipApplication, ContactMessage

class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address',
            'date_of_birth', 'previous_employer', 'retirement_date',
            'reason_for_joining'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'previous_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'retirement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason_for_joining': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        } 