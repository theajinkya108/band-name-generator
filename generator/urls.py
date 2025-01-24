from django.urls import path
from . import views

urlpatterns = [
    path('',views.band_name_generator, name = "band_name_generator"),
]