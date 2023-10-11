from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name='home'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),

    path('404', views.error404, name='404'),


    path('account/my_account', views.my_account, name='my_account'),
    path('account/register', views.register, name='register'),
    path('account/login', views.login, name='login'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)