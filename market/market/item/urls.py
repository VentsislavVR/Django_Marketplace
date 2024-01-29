from django.urls import path, include

from market.item import views

# app_name = 'item'
urlpatterns = (
    path('', views.browse, name='browse'),
    path('new/', views.add_item, name='add_item'),
    path('<int:pk>/',include([
        path('', views.item_detail, name='detail'),
        path('edit/', views.edit_item, name='edit_item'),
        path('delete/', views.delete_item, name='delete_item'),

    ])),
)
