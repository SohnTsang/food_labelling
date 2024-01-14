from django.urls import path
from . import views

urlpatterns = [
    path('create-label/', views.create_label_template, name='create_label_template'),
    path('result/', views.result_page, name='result_page'),
]