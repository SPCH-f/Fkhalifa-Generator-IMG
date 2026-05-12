from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('api/generate/', views.generate_image, name='generate_image'),
    path('api/delete/', views.delete_image, name='delete_image'),
    path('api/suggestions/', views.get_suggestions, name='get_suggestions'),
]
