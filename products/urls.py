from django.urls import path

from products.views import ProductsDetailView, ProductsListView, WishlistListView, add_wishlist, add_to_cart, \
    CartListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_wishlist, name='add-wishlist'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail'),
]
