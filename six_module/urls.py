from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('blog/', include('posts.urls', namespace='posts')),
    path('api/', include('api.urls', namespace='api')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('profile/', include('users.urls', namespace='profile')),
    path('products/', include('products.urls', namespace='products')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
