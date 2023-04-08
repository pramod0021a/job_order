from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index_page, name='home'),    
    path('export/', views.export, name='export'),
]