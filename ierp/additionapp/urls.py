from django.urls import path
from . import views
urlpatterns=[
    path('',views.add,name='index'),
    path('sub',views.sub,name='sub')
]