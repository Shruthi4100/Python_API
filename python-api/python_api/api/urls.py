from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipe_list, name='recipe-list'),
    path('contact/',views.contact_list, name='contact-list'),
]
