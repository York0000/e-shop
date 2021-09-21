from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, ListView

from pages.forms import ContactModelForm, FAQModelForm
from pages.models import EmployeeModel, FAQModel
from posts.models import PostModel


from products.models import ProductModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        context['products'] = ProductModel.objects.order_by('-pk')[:3]
        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['employees'] = EmployeeModel.objects.order_by('-pk')[:4]

        return context


class MiniCartListView(ListView):
    template_name = 'layouts/header.html'

    def get_queryset(self):
        return self.request.session.get('cart', [])


class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'


class FAQListView(ListView):
    template_name = 'faq.html'

    queryset = FAQModel.objects.all()
