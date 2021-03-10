from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.index, name="home"),
    path("register/", views.register, name="register"),
    path("product/<str:uid>", views.product_details, name="product.details"),
    path("sign_in/", views.sign_in, name="login_action")
]
