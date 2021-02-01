from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .models import *
import datetime

def index(request):
	s1_labels = []
	s1_data = []
	s1_queryset = Data_Terminal.objects.filter(switch_label='S1')
	s2_labels = []
	s2_data = []
	s2_queryset = Data_Terminal.objects.filter(switch_label='S2')
	s3_labels = []
	s3_data = []
	s3_queryset = Data_Terminal.objects.filter(switch_label='S3')
	
	for data_terminals in s1_queryset:
		s1_labels.append(data_terminals.time_stamp.strftime(('%Y-%m-%dT%H:%M:%S.%f%z')))
		s1_data.append(data_terminals.switch_status)

	for data_terminals in s2_queryset:
		s2_labels.append(data_terminals.time_stamp.strftime(('%Y-%m-%dT%H:%M:%S.%f%z')))
		s2_data.append(data_terminals.switch_status)

	for data_terminals in s3_queryset:
		s3_labels.append(data_terminals.time_stamp.strftime(('%Y-%m-%dT%H:%M:%S.%f%z')))
		s3_data.append(data_terminals.switch_status)

	context = {
		's1_labels':s1_labels,
		's1_data':s1_data,
		's2_labels':s2_labels,
		's2_data':s2_data,
		's3_labels':s3_labels,
		's3_data':s3_data,
	}

	return render(request, 'monitor/index.html', context)

def data_terminal_list(request):
	#data_terminals = Data_Terminal.objects.filter(t1_status=0,t2_status=0,t3_status=0,t4_status=0,t5_status=0)
	data_terminals = Data_Terminal.objects.filter(switch_status=0)
	context={
		"data_terminals":data_terminals,
	}
	return render(request, 'monitor/list.html', context)

class upload(SuccessMessageMixin, CreateView):
    model = Data_Terminal_BulkUpload
    template_name = 'monitor/upload.html'
    fields = ['csv_file']
    success_url = reverse_lazy('list')
    success_message = 'Successfully uploaded Data'