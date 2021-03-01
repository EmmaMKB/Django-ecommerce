from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.index, name="home"),
    path("register/", views.register, name="register"),
    path("product/details/<str:uid>", views.product_details, name="product.details")
]
