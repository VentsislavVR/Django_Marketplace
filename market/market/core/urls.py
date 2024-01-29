from django.urls import path

from market.core.views import index, contact, signup, SignInView

urlpatterns = (
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', SignInView.as_view(), name='login'),

)
