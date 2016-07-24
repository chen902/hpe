from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = form.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'employee_num', 'password']