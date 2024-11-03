from .models import CollaborateRequest
from django import forms 

class CollaborationForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message', )
