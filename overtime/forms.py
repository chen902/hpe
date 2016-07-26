from django.contrib.auth.models import User
from overtime.models import Event
from django import forms
from django.conf import settings

from django.forms import widgets


# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)
#
# 	class Meta:
# 		model = User
# 		fields = ['username', 'employee_num', 'password']
TYPES = (
	(1, 'כונן יום חול'),
	(2, 'כונן סוף שבוע'),
	(3, 'שעות נוספות'),
	(4, 'הקפצה'),
)


class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ['type', 'description', 'start_date', 'end_date', 'duration']

		widgets = {
			'start_date': forms.DateTimeInput(attrs={'class': 'input-group date', 'id': 'datetimepicker1'}),
			'end_date': forms.DateTimeInput(attrs={'class': 'input-group date', 'id': 'datetimepicker2'}),
		}

# 		widgets = {
# 			'start_date': forms.DateTimeInput(attrs={'class': 'datetimepicker1'})
# 		}
#
# 	def __init__(self, *args, **kwargs):
# 		self.fields["report"] = forms.CharField(widget=forms.HiddenInput)
# 		super(EventForm, self).__init__(self, *args, **kwargs)


