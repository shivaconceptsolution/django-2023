from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('contactus',views.contactus,name='contactus'),
    path('gallery',views.gallery,name='gallery'),

]