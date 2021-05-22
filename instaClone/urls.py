from django.urls import path, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView




from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),






  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))




]