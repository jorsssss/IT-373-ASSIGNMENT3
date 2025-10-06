from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.announcements_list, name='announcements_list'),
    path('announcements/<int:id>/', views.announcements_detail, name='announcement_detail'),
]
