from django.urls import path, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView




from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  path('like/<int:pk>', views.like,name='like_image'),
  path('profile/<username>/', views.user_profile, name='profile_page'),
  re_path(r'^upload_image/', views.upload_image, name='upload_image'),
  






  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))




]