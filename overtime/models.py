from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


PERCENTAGE = {
	(1, '100%'),
	(1.5, '150%'),
	(2, '200%'),
	(2.5, '250%'),
	(3, '300%'),
	(4, '400%')
}


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


class Type(models.Model):
	name = models.CharField(max_length=100)
	predefined_value = models.IntegerField(blank=True, null=True)
	percentage = models.FloatField(choices=PERCENTAGE)

	def __str__(self):
		str_name = self.name + " - " + dict(PERCENTAGE).get(self.percentage)
		if self.predefined_value:
			str_name += " - " + str(self.predefined_value) + " שעות"
		return str_name


class Event(models.Model):
	type = models.ForeignKey(Type, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, blank=True)
	start_date = models.DateTimeField('Date')
	end_date = models.DateTimeField(blank=True)
	duration = models.IntegerField()
	report = models.ForeignKey(Report, on_delete=models.CASCADE)

	def __str__(self):
		return self.type




