from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from overtime.forms import EventForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
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
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save(commit=False)
			event.report = get_object_or_404(Report, pk=report_id)
			event.save()
			return redirect('overtime:report', pk=report_id)
	else:
		form = EventForm()
	return render(request, 'overtime/event_edit.html', {'form': form, 'report_id': report_id})


def event_edit(request, pk):
	event = get_object_or_404(Event, pk=pk)
	if request.method == "POST":
		form = EventForm(request.POST, instance=event)
		if form.is_valid():
			event = form.save(commit=False)
			event.report = get_object_or_404(Report, pk=event.report.pk)
			event.save()
			return redirect('overtime:report', pk=event.report.pk)
	else:
		form = EventForm(instance=event)
	return render(request, 'overtime/event_edit.html', {'form': form})


class EventDelete(DeleteView):
	model = Event

	def get_success_url(self):
		event = self.object
		return reverse_lazy('overtime:report', kwargs={'pk': event.report.pk})
