from django import forms
from .models import Morpheme

class MorForm(forms.ModelForm):

    class Meta:
        model = Morpheme
        fields = ('text', 'words', )
