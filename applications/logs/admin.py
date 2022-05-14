from django.contrib import admin
from .models import *


class LogAdmin(admin.ModelAdmin):
    fields = ['id', 'text', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

    search_fields = []
    list_display = ['text', 'created_at']

    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(Log, LogAdmin)
