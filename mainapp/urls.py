from django.urls import path
from .views import products, product
# from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    # path('category/<int:pk>/', cache_page(3600)(products), name='category'),
    path('category/page/<int:page>/', products, name='page'),
    path('<int:pk>/', product, name='detail'),
]