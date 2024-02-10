from django import forms
from .models import Links

class LinkForm(forms.ModelForm):
        
    link = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your URL here...'}))
    
    class Meta:
        model = Links
        fields = ['link']
        labels = {'link': ''}
        widgets = {
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your URL here...'})
        }