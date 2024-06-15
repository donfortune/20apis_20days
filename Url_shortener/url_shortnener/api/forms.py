from django import forms
from .models import urlModel

class URLForm(forms.ModelForm):
    class Meta:
        model = urlModel
        fields = ['original_url']
