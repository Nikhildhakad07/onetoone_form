from django import forms
from .models import user,profile

class userform(forms.ModelForm):
    class Meta:
        model=user
        fields = '__all__'
        

class Profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields = '__all__'
    