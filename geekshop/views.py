from django.shortcuts import render


def index(request):
    context = render(request, 'geekshop/index.html')
    return context


def contacts(request):
    return render(request, 'geekshop/contact.html')