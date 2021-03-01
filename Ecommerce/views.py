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


def product_details(request, uid):
    try:
        product = ProductDao.get_product(uid)
    except:
        product = None

    return render(request, 'product/product.details.html', {
        'product': product,
        'product_exists': product != None,
    })
