from django.urls import path
from index import views

app_name = 'cicd'

urlpatterns = [
    path('', views.first, name='first'),
]