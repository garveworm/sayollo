from django.urls import path

from . import views

urlpatterns = [
    path('ads/', views.GetAd.as_view(), name="ads"),
    path('impressions/', views.Impressions.as_view(), name="impressions"),
    path('stats/', views.GetStats.as_view(), name="stats"),
]