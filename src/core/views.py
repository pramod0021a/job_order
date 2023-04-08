import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job
from .forms import JobForm
# Create your views here.

def index_page(request):
   if request.method == 'POST':
      fm = JobForm(request.POST)
      if fm.is_valid():
         fm.save()         
         fm = JobForm()
   else:
      fm = JobForm()

   # qs = Job.objects.all()
   qs = Job.objects.order_by('-id')
   context = {
      'jobs':qs,
      'form':fm,
   }
   return render(request, 'core/index.html', context)

def export(request):
   response = HttpResponse(content_type='text/csv')

   writer = csv.writer(response)
   writer.writerow([ 'Date', 'Customer Name', 'Item Name', 'Quantity', 'Price', 'Total Price'])

   for item in Job.objects.all().values_list( 'date', 'customer_name', 'item_name', 'quantity', 'price', 'total_price'):
      writer.writerow(item)

   response['Content-Disposition'] = 'attachment; filename="order.csv"'

   return response