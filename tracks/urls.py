from django.urls import path
from . import views


app_name = 'tracks'

urlpatterns = [
    path('list/', views.music_list, name='list'),
    path('create/', views.music_create, name='create'),
    path('detail/<int:pk>/', views.music_detail, name='detail'),
    path('delete/<int:pk>/', views.music_delete, name='delete'),
    path('update/<int:pk>/', views.music_update, name='update'),
]