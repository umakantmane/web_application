from django import forms
from django.core.validators import ValidationError


#
# def validateName(value):
#
#     if value.isdigit():
#         raise ValidationError('Name cannot be in numbers!')
#
# def validateEamil(value):
#
#     if value.find('@mytectra.com')<0:
#         raise ValidationError('Please provide email with mytectra.com only!')
#

class UserForm(forms.Form):

    city = (
        ('', '--Select option--'),
        ('cn', 'Chennai'),
        ('bng', 'Bangalore'),
        ('hyd', 'Hyderabad')
    )
    gn = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    is_active = forms.CharField(widget=forms.CheckboxInput)
    is_active2 = forms.BooleanField()
    mul = forms.MultipleChoiceField(
        choices=city,
        widget=forms.CheckboxSelectMultiple
    )
    user_city = forms.ChoiceField(choices=city)
    username = forms.CharField(
        label='Name',
        required=True,
        help_text='Proivde valid user name',
        min_length=8,
        max_length=20,
        error_messages={
            'required':'Username cannot blank!',
            'min_length':'Please provide atleast 8 characters'
        },
        initial='Manas',
        #validators=[validateName]
    )
    email = forms.EmailField(
        #validators=[validateEamil]
    )
    address = forms.CharField(widget=forms.Textarea)
    password1 = forms.CharField()
    password2 = forms.CharField()


    def clean(self):

        form_data = self.cleaned_data
        if 'username' in form_data:
            if form_data['username'].isdigit():

                self.errors['username'] = ['Invalid username!']

        if 'password1' in form_data  and 'password2' in form_data:

            if form_data['password1'] != form_data['password2']:
                self.errors['password2'] = ['Password mismatch!']

        return form_data