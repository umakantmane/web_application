from django import forms
from form_example.models import Collage
from django.core.validators import ValidationError


def validateName(name):

    if name.isdigit():

        raise ValidationError("Invalid name!")

class CollageForm(forms.ModelForm):

    name = forms.CharField(
        min_length=8,
        max_length=20,
        validators=[validateName]
    )
    address = forms.CharField(widget=forms.Textarea)
    class Meta:

        model = Collage
        #fields = '__all__'
        #or
        fields = ('name', 'email', 'address','city')
