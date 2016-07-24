from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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