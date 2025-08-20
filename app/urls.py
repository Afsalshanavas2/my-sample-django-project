from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student_list/', views.student_list, name='student_list'),
    path('search/', views.search_students, name='search_students'),
]