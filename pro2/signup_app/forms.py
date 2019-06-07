from django import forms
from django.core import validators
from . models import Signup_model
# build in validators
# value- parameter-relaize django that it ts a validator
def chek_for_z(value):
    if value[0]!='z':
        raise forms.ValidationError('noit startivg with z')

class Signupform_1(forms.Form):
    user_name = forms.CharField(validators=[chek_for_z])
    mobile_number=forms.IntegerField(widget=forms.NumberInput)

    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    bot = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean_bot(self):
        bot = self.cleaned_data['bot']
        if len(bot)>0:
            raise forms.ValidationError('COught u')
        return bot

    def clean(self):
        all_cleandata=super().clean()
        p1= self.cleaned_data['password']
        p2= self.cleaned_data['password2']
        if p1 != p2:
            raise forms.ValidationError("password not matching")
        # return p1

class Signupmodel_form(forms.ModelForm):
    class Meta:
         model = Signup_model
         fields = '__all__'
