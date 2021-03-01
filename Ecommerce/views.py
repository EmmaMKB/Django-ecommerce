from django.shortcuts import render
from Ecommerce.dao import subcategory

SubcategoryDao = subcategory.SubCategoryDao()


def index(request):
    
    subcategories = SubcategoryDao.get_all()
    return render(
        request, 
        'index.html', {
            'subcategories': subcategories
        })
