from django import forms

from PersonalPage.models import *


class EditRecordingForm(forms.ModelForm):
    class Meta:
        model = User_Recording_Sell
        fields = ['artist', 'recording', 'description', 'price']


    def clean_artist(self):
        return self.cleaned_data['artist']

    def clean_recording(self):
        return self.cleaned_data['recording']

    def clean_description(self):
        return self.cleaned_data['description']

    def clean_price(self):
        return self.cleaned_data['price']
