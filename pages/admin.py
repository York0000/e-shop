from django.contrib import admin

from pages.models import ContactModel, EmployeeModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'phone', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'email', 'position']
