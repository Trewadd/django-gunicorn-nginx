from django.urls import path

from . import views

urlpattern = [
        path('atricles/<int:year>/', views.year_archive),
        path('articles/<int:year>/<int:month>/', views.month_archive),
#        path('articles/<int:year>/<int:month>/<int:pk>/', views.article.detail),
        ]
