from django.contrib import admin
from django.urls import path, include
from store.views import *
from accounts.views import *
from django.conf.urls.static import static
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('cart/', cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('product/<str:slug>/', product_details, name='details'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
