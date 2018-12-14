from django import forms
from django.forms import ModelForm
from .models import LawFile

class LawFileForm(ModelForm):
    class Meta:
        model = LawFile
        fields = ['type_law', 'number_law', 'date_publish', 'name_law', 'desc_law', 'file_law']

class SearchForm(forms.Form):
    query = forms.CharField()