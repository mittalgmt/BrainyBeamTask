from django.urls import path
from . import views

urlpatterns = [
    path('save-data/', views.save_data, name='save_data'),
]
