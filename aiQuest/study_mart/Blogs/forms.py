from django import forms
from django.core import validators

class TeacherRegistration(forms.Form):
    first_name = forms.CharField(label='Enter your first Name', label_suffix=' ') # label_suffix is (:) if want to remove keep it (' ')empty
    last_name = forms.CharField(initial='StudyMart',required=True)
    email = forms.EmailField(initial='r@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    txtArea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkBox = forms.CharField(widget=forms.CheckboxInput)
    
    
    
    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']       
        repass = self.cleaned_data['repassword']       
        if rightpass != repass:
            raise forms.ValidationError('Password dose not match')