from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from ecoapp.models import Product,Category,Basket_card,Brend,NutritionValue,Header,Blog,HomeAbout,HomeIcons,Partners
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
from django.db.models import F
def set_language(request, lang_code):
    url = request.META.get("HTTP_REFERER", None)
    if lang_code == 'az':
        return HttpResponseRedirect('/')
    else:
        response = redirect(translate_url(url, lang_code))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    
def home(request):
    headers = Header.objects.all()
    blogs = Blog.objects.all()
    if len(blogs)>4:
        blogs = blogs[0:4]
    about = HomeAbout.objects.first()
    icons = HomeIcons.objects.all()
    partners = Partners.objects.all()
    products = Product.objects.annotate(result=F('price') - F('discount_price'))
    categories = Category.objects.all()
    context = {
        'products':products,
        'headers':headers,
        'blogs':blogs,
        'about':about,
        'icons':icons,
        'partners':partners,
        'categories':categories
    }
    return render(request,'index.html',context)

def account(request):
    context = {}
    return render(request,'Account.html',context)