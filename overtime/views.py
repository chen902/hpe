from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from overtime.forms import EventForm
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Report, Event

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'overtime/index.html'
	context_object_name = 'all_reports'

	def get_queryset(self):
		return Report.objects.all()


class DetailView(generic.DetailView):
	model = Report 
	template_name = 'overtime/report.html'


class ReportCreate(CreateView):
	model = Report
	fields = ['name', 'employee_id']


class ReportUpdate(UpdateView):
	model = Report
	fields = ['name', 'employee_id']


#class ReportDelete(DeleteView):
#	model = Report
#	success_url = 'overtime:index'


def event_create(request, report_id):
	form = EventForm()
	return render(request, 'overtime/event_edit.html', {'form': form, 'report_id': report_id})



