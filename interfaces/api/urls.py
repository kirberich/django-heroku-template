from django.urls import path

from .views import example as example_views

urlpatterns = [
    path('example/<instance_id>', example_views.example_detail, name='example-detail'),
]
