from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import authenticate,logout,login

def home(request):
    sliders = Slider.objects.all().order_by('-id')[0:6]
    banner = Banner.objects.all().order_by('-id')[0:3]
    main_category = Main_category.objects.all().order_by('-id')
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')
    product = Product.objects.filter(section__name = "Top Deals Of The Day")
    

    context = {
        'sliders': sliders,
        'banner': banner,
        'main_category': main_category,
        'category': category,
        'sub_category': sub_category,
        'product': product,
    }
    return render(request, 'home.html', context)


def product_details(request,slug): 

    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'product': product,
    }   
     
    return render(request, 'product/product_detail.html',context)



def error404(request):     
     
    return render(request, 'error/404.html')


def my_account(request):     
     
    return render(request, 'account/my_account.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()    
    return redirect('my_account')



    
    


