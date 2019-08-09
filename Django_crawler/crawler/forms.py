from django import forms
from .models import SearchRecord,Key,Article


class SearchRecordForm(forms.ModelForm):
    class Meta:
        model = SearchRecord
        fields = (
             'content_string', 
        )
