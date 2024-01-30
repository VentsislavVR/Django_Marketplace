from django.urls import path

from market.conversation import views

urlpatterns = (
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.conversation_detail, name='conversation_detail'),
    path('new/<int:pk>/', views.new_conversation, name='new_conversation'),

)