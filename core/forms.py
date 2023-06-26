from tkinter import Widget
from attr import field
from django import forms
from .models import *
class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','roll','city')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }