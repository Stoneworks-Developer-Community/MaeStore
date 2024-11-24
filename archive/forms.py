from django import forms
from Testament.settings import TESTAMENT_WORLDS, TESTAMENT_GENRES

class BookUploadForm(forms.Form):
    file = forms.FileField()
    world = forms.ChoiceField(choices=TESTAMENT_WORLDS)
    genre = forms.ChoiceField(choices=TESTAMENT_GENRES)
