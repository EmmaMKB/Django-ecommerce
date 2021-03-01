from django.shortcuts import render
from Ecommerce.dao import subcategory, product

SubcategoryDao = subcategory.SubCategoryDao()
ProductDao = product.ProductDao()


def index(request):
    
    subcategories = SubcategoryDao.get_all()
    last_products = ProductDao.get_lasts()
    return render(
        request, 
        'index.html', {
            'subcategories': subcategories,
            'last_products': last_products
        })


def register(request):

    return render(request, 'auth/register.html')
