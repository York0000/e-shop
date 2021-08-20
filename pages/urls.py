from django.urls import path

from pages.views import ContactCreateView, AboutTemplateView, HomeTemplateView, PrivacyTemplateView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('privacy/', PrivacyTemplateView.as_view(), name='privacy'),
    path('', HomeTemplateView.as_view(), name='home'),
]
