from .models import Job
from django import forms

class JobForm(forms.ModelForm): 
   class Meta: 
      model = Job 
      fields = ['customer_name', 'item_name', 'quantity', 'price']
      widgets = {'customer_name':forms.TextInput(attrs={'class':'form-control'}), 
               'item_name':forms.TextInput(attrs={'class':'form-control'}),
               'quantity':forms.TextInput(attrs={'class':'form-control'}),
               'price':forms.TextInput(attrs={'class':'form-control'}),
               }