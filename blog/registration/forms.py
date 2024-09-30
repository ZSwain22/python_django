from django import forms
from registration.models import UserInfo

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserInfo
        fields = '__all__'
        
class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = UserInfoForm
        fields = ('username', 'password')