from django.urls import path, include
from . import views

app_name = 'chollo_main'


urlpatterns = [
    # views
    path("", views.home, name='home'),

    # # login
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    # # PasswordChange
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # # PasswordReset
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/uidb64/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView(), name='password_reset_complete'),

    # the whole auth could be replaced with the following line
    path('', include('django.contrib.auth.urls')),

    # other urls
    path("product_list/", views.product_list, name='product_list'),
    path("product_list/<slug:category_slug>", views.product_list, name='product_list_by_category'),
    path("product_detail/<int:id>/<slug:slug>", views.product_details, name='product_detail'),
    path("register/", views.register, name='register'),
    # path("cart_details/", views.cart_details, name='cart_details'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.item_search, name='item_search'),

]

