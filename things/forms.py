"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']  # Exclude 'created_at'

    # Customize form fields
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength':120}))
    quantity = forms.IntegerField(widget=forms.NumberInput)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0 or quantity > 100:
            raise forms.ValidationError("Quantity must be between 0 and 100.")
        return quantity


