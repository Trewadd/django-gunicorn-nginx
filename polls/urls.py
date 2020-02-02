from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:quetion_id>/', views.detail, name='detail'),
        path('<int:quetion_id>/results/', views.result, name='results'),
        path('<int:qustion_id>/vote/', views.vote, name='vote'),
        ]
