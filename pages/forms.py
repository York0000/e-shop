from django import forms

from pages.models import ContactModel, LeaveFAQModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']


class FAQModelForm(forms.ModelForm):
    class Meta:
        model = LeaveFAQModel
        fields = '__all__'
