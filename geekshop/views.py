from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def index(request):
    products = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # if pk:
        #     if pk == '0':
        #         products = Product.objects.all().order_by('price')
        #         category = {'name': 'все'}
        #     else:
        #         category = get_object_or_404(ProductCategory, pk=pk)
        #         products = Product.objects.filter(category__pk=pk).order_by('price')

    context = {
        'title': 'главная',
        # 'links_menu': links_menu,
        # 'category': category,
        'products': products,
        'basket': basket,
    }

    return render(request, 'geekshop/index.html',context)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'контакты',
        'basket': basket,
    }

    return render(request, 'geekshop/contact.html', context)