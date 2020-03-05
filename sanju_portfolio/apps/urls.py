from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='Home'),
    path('About/' ,views.about_view ,name='about'),
    path('Contact/', views.contact_view, name='contact'),
]