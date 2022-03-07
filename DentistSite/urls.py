from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact.html', views.contact, name = 'contact'),
    path('pricing', views.pricing, name = 'pricing'),
    path('service', views.service, name = 'service'),
    path('appointment', views.appointment, name = 'appointment'),
]