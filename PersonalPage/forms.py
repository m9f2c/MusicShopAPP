from django import forms
from PersonalPage.views import *
from PersonalPage.models import *

class EditRecordingForm(forms.ModelForm):
    class Meta:
        model =  User_Recording_Sell
        fields = ['artist', 'recording', 'description', 'price']

    artist = forms.CharField(max_length=140, label='artist',required=True)
    recording = forms.CharField(max_length=140, label='artist',required=True)
    description = forms.Textarea
    price = forms.CharField(max_length=140, label='artist',required=True)

    def clean_artist(self):
        return add_artist('artist')

    def clean_recording(self):
        return self.cleaned_data['recording']

    def clean_description(self):
        return self.cleaned_data['description']

    def clean_price(self):
        return self.cleaned_data['price']