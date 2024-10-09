from django.contrib import admin
from .models import Products, ProductImage, Basket, Categories, FavouriteProduct, ProductColor, Subcategory, Messages


admin.site.register(ProductImage)
admin.site.register(Products)
admin.site.register(Basket)
admin.site.register(Categories)
admin.site.register(FavouriteProduct)
admin.site.register(ProductColor)
admin.site.register(Subcategory)
admin.site.register(Messages)
