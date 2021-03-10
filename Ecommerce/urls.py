from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.index, name="home"),
    path("register/", views.register, name="register"),
    path("sign_in/", views.sign_in, name="login_action"),
    path("logout/", views.logout_user, name="logout"),
    path("products/", views.products, name="products"),
    path("products/category/<str:uid>", views.products_by_category, name="product.category"),
    path("product/<str:uid>", views.product_details, name="product.details"),
]
