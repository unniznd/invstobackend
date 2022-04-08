from django.contrib import admin

from handler.models import Stock

@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    list_display = ['datetime','close','high','low','open','volume','instrument']
