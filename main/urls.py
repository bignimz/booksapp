from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name='home'),
    path("about-us/", TemplateView.as_view(template_name="about.html"), name='about-us'),
    path("contact-us/", views.ContactUsView.as_view(template_name="contact.html"),
         name='contact-us'),

]
