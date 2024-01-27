from django.urls import path

from market.core.views import index, contact

urlpatterns = (
    path('', index, name='index'),
    path('contact/', contact, name='contact'),

)