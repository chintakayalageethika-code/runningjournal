from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('progress/', views.progress, name='progress'),
    path('strava/', views.strava_runs, name='strava_runs'),
]