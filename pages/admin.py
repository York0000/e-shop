from django.contrib import admin

from pages.models import ContactModel, EmployeeModel, FAQModel, LeaveFAQModel


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


@admin.register(FAQModel)
class FAQModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    list_filter = ['question', 'answer']
    search_fields = ['question', 'answer']


@admin.register(LeaveFAQModel)
class LeaveFAQModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'name', 'phone']
    list_filter = ['question']
    search_fields = ['question', 'name', 'phone']
