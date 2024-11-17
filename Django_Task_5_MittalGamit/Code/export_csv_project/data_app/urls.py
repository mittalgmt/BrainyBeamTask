from django.urls import path
from .views import export_items_csv

urlpatterns = [
    path('export-csv/', export_items_csv, name='export_items_csv'),
]
