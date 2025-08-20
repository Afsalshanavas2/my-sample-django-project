from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name='products'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('search_teacher/', views.search_teachers, name='search_teachers')
]