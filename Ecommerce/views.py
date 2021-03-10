from pprint import pprint

from django.shortcuts import render, redirect
from django.urls import reverse

from Ecommerce.dao import subcategory, product
from .forms import RegisterForm, LoginForm
from .models import Person
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate, login, logout

SubcategoryDao = subcategory.SubCategoryDao()
ProductDao = product.ProductDao()


def index(request):

    form = LoginForm()
    subcategories = SubcategoryDao.get_all()
    last_products = ProductDao.get_lasts()
    return render(
        request, 
        'index.html', {
            'subcategories': subcategories,
            'last_products': last_products,
            'form': form
        })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            hasher = PBKDF2PasswordHasher()
            salt = hasher.salt()
            password = hasher.encode(form.cleaned_data.get('password'), salt)
            email = form.cleaned_data.get('email')
            user = Person()
            user.email = form.cleaned_data.get('email')
            user.password = password
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.phone = form.cleaned_data.get('phone')
            user.save()
            user = authenticate(request, username=email, password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect("home")

        else:
            render(request, 'auth/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("email"), password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, 'index.html', {'login_error': True})

    return redirect("home")


def product_details(request, uid):
    try:
        product = ProductDao.get_product(uid)
    except:
        product = None

    return render(request, 'product/product.details.html', {
        'product': product,
        'product_exists': product != None,
    })
