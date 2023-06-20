from django.urls import path
from . import views

app_name = 'chollo_main'


urlpatterns = [
    # views
    path("", views.home, name='home'),
    path("product/", views.product, name='product'),
    path("signin/", views.signin, name='signin'),
    path("signup/", views.signup, name='signup'),
    path("cart_details/", views.cart_details, name='cart_details'),

]