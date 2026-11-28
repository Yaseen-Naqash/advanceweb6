from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def home(request):

    products = Product.objects.all()



 

    context = {
        'age' : 12,
        'name' : 'john',
        'isLogin' : False,
        'products' : products,
    }
    return render(request, 'index.html', context)


def profile(request):
    skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Django']
    courses = [
        {'title': 'Math', 'score': 18},
        {'title': 'Physics', 'score': 15},
        {'title': 'Chemistry', 'score': 10},
        {'title': 'Biology', 'score': 19},
    ]

    context = {
        'username': 'sara',
        'age': 17,
        'is_active': True,
        'is_admin': False,
        'skills': skills,
        'courses': courses,
        'favorite_language': 'Python',
        'empty_list': [],
    }
    return render(request, 'profile.html', context)


def detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)



def products(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    category_query = request.GET.get('category')
    print(category_query)
    # request.POST.get('q')
 

    products = Product.objects.filter(title__contains = q)

    categories = Category.objects.all()
    context = {
        'products': products,
        'categories' : categories
    }
    return render(request, 'search_filter.html', context)
