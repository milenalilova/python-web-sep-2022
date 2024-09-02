from django import forms

from MyPlantApp.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
