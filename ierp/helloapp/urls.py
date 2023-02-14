from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('marksheet',views.marksheet,name='marksheet')
]