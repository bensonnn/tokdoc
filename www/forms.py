from django import forms       
from django.contrib.auth.models import User


class TokDocEmail(forms.EmailField):
    def validate(self, value): 
        super(TokDocEmail, self).validate(value)

        users = User.objects.filter(email=value)
        if len(users)>0:       
            raise forms.ValidationError('email already used')
      
class PatientSignupForm(forms.Form):
    email = TokDocEmail()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
  
class DoctorSignupForm(forms.Form):
    email = TokDocEmail()      
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    
class UserLogin(forms.Form):   
    email = forms.EmailField() 
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)



