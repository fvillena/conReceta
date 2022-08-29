from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:concept_id>/', views.detail, name='detail'),
    path('search', views.search_results, name='search_results'),
]