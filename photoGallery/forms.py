from django import forms
from .models import Photograph


class PhotographForm(forms.ModelForm):
    class Meta:
        model = Photograph
        fields = ('name', 'location', 'photographer', 'date', 'image')
        #use widgets to add new functionalities like form-control
    
class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())