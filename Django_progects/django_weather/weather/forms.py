from django.forms import ModelForm, TextInput

from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']

        # mapping in index.http
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Input city'
        })}
