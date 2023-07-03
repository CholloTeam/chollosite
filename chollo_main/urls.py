from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chollo_main'


urlpatterns = [
    # views
    path("", views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("product_list/", views.product_list, name='product_list'),
    path("product_list/<slug:category_slug>", views.product_list, name='product_list_by_category'),
    path("product_detail/<int:id>/<slug:slug>", views.product_details, name='product_detail'),
    path("signin/", views.signin, name='signin'),
    path("signup/", views.signup, name='signup'),
    path("cart_details/", views.cart_details, name='cart_details'),

]

