from django.urls import path

from market.dashboard.views import dashboard

urlpatterns = (
    path('', dashboard, name='dashboard'),
)
