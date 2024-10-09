from django.urls import path
from .views import index, favorite_products, basket, basket_add, basket_remove, product_search, add_favourite, product_info, delete_favourite, about, contact


urlpatterns = [
    path('', index, name='index'),
    path('filter/<int:sub_id>', index, name='filter'),
    path('favorites/', favorite_products, name='favorites_products'),
    path('basket/', basket, name='basket'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('search/', product_search, name='product_search'),
    path('favourites/add/<int:product_id>/', add_favourite, name='add_favourite'),
    path('product/<int:product_id>/', product_info, name='product_info'),
    path('favourites/remove/<int:product_id>/', delete_favourite, name='delete_favourite'),
    path('about_us', about, name='about'),
    path('contacts', contact, name='contact')
]
