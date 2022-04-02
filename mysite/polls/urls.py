from django import views
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('overall_score/', views.overall_score, name='overall_score'),
    path('insert/', views.insert, name='insert'),
    path('<int:question_id>/insert_choice/', views.insert_choice, name='insert_choice'),
]