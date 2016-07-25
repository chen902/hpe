from django.contrib.auth.models import User
from overtime.models import Event
from django import forms


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'employee_num', 'password']


# class EventForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Event
# 		fields = ['type', 'description', 'end_date', 'duration']
# 		widgets = {
# 			'start_date': forms.DateTimeInput(attrs={'class': 'datetimepicker1'})
# 		}
#
# 	def __init__(self, *args, **kwargs):
# 		self.fields["report"] = forms.CharField(widget=forms.HiddenInput)
# 		super(EventForm, self).__init__(self, *args, **kwargs)


