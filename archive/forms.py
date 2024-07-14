from django import forms
from MaeStore.settings import MAESTOR_WORLDS, MAESTOR_GENRES

class BookUploadForm(forms.Form):
    file = forms.FileField()
    world = forms.ChoiceField(choices=MAESTOR_WORLDS)
    genre = forms.ChoiceField(choices=MAESTOR_GENRES)
