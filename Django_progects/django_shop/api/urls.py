from django.urls import path

from . import views

urlpatterns = [
    path('ads/<int:pk>/comments', views.comments),
    path('ads/<int:pk>/', views.AdsDetailView.as_view()),
    path('ads/', views.ads),
]