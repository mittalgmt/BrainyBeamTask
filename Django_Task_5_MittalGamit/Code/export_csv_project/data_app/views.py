import csv
from django.http import HttpResponse
from .models import Item

def export_items_csv(request):
    # Create the HttpResponse object with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(['Name', 'Description', 'Created At'])

    # Write data rows
    items = Item.objects.all()
    for item in items:
        writer.writerow([item.name, item.description, item.created_at])

    return response
