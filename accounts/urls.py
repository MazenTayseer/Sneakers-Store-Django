from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('logIn/', views.log_in, name="log_in"),
    path('signUp/', views.sign_up, name="sign_up"),
    path('logout/', views.logout_user, name="logout"),

    path('shop/', views.shop, name="shop"),
    path('view/<int:pk>/', views.view_product, name="view"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('removeItem/<int:pk>/', views.remove_product, name="remove_product"),
    path('ship_order/<int:pk>/', views.ship_order, name="ship_order"),

    path('dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('addProduct/', views.add_product, name="add_product"),
    path('deleteProduct/<int:pk>/', views.delete_product, name="delete_product"),
    path('updateProduct/<int:pk>/', views.update_product, name="update_product"),

]
