from django.contrib import admin

from .models import Stock
from .forms import StockModelForm


class StockAdmin(admin.ModelAdmin):
    readonly_fields = ['sku', "date_added", "date_modified"]
    form = StockModelForm
    list_filter = ['name', 'quantity']


admin.site.register(Stock, StockAdmin)
