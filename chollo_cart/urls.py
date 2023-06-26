from django.urls import path

from chollo_cart import views

app_name = 'chollo_cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>?', views.remove_from_cart, name='remove_from_cart'),
    ]
