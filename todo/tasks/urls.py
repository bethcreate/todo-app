from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns = [
    path('', views.index, name='list'),

    path('update_task/<str:pk>/', views.UpdateTask, name='updateTask'),
    path('delete/<str:pk>/', views.UpdateTask, name='delete'),
]