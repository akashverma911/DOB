from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import DobForm
from django.http import HttpResponse
from datetime import date
from dateutil.relativedelta import relativedelta
import json
class FindDobView(FormView):
  template_name = 'app/dob.html'
  form_class = DobForm
  success_url = ''
  
  def form_valid(self, form):
    

      rdelta = relativedelta(date.today(), form.cleaned_data['date_of_birth'])
      print('Age in years - ', rdelta.years)
      print ('Age in months - ', rdelta.months)
      print ('Age in days - ', rdelta.days)
      print(form.cleaned_data['date_of_birth'])
      today = date.today()
      print(rdelta)
      entry = {}
      entry['years'] = rdelta.years
      entry['months'] = rdelta.months
      entry['days'] = rdelta.days
      json_data = json.dumps(entry)
      return HttpResponse(json_data)

  
