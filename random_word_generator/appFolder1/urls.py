from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('generate',views.index2),
    path('reset',views.index1),
]