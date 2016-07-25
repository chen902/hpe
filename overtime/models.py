from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your models here.
class Report(models.Model):
	name = models.CharField(max_length=20)
	employee_id = models.IntegerField()
	is_submited = models.BooleanField(default=False)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	
	def get_absolute_url(self):
		return reverse('overtime:report', kwargs={'pk': self.pk})
		
	def __str__(self):
		return self.name

	def get_year(self):
		if self.event_set:
			return self.event_set.all()[0].start_date.date().year



	
class Event(models.Model):
	type = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	start_date = models.DateTimeField('Date')
	end_date = models.DateTimeField(blank=True)
	duration = models.IntegerField()
	report = models.ForeignKey(Report, on_delete=models.CASCADE)
	def __str__(self):
		return self.type
		
		
