from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'data'),
    path('delete/', views.delete),
    path('update/<str:pk>/', views.update, name = 'update')

]