"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.Form):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description':forms.Textarea(), 'quantity':forms.NumberInput(attrs={'min': 0, 'max': 100})}


