from django.shortcuts import render
from mainapp.models import Product


def product(request, pk):
    print(pk)
    return


def products(request):
    links_menu = [
        {'href': '', 'name': 'все'},
        {'href': '', 'name': 'дом'},
        {'href': '', 'name': 'офис'},
        {'href': '', 'name': 'модерн'},
        {'href': '', 'name': 'классика'},
    ]
    context = {
        'title': 'каталог',
        'links_menu': links_menu,
        'object': Product.objects.get(id=2)
    }
    return render(request, 'mainapp/products.html', context=context)
