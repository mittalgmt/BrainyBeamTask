import csv
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from .models import Item
from django.contrib import admin


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'export_button')

    # Add a custom action for export
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Action to export selected items to CSV.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_items.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Description', 'Created At'])
        for item in queryset:
            writer.writerow([item.name, item.description, item.created_at])

        return response

    export_as_csv.short_description = "Export Selected Items to CSV"

    def export_button(self, obj):
        """
        Adds a button in the Admin interface to trigger the CSV export.
        """
        url = reverse('export_items_csv')
        return format_html('<a class="button" href="{}">Export All to CSV</a>', url)

    export_button.short_description = "Export Button"
    export_button.allow_tags = True
