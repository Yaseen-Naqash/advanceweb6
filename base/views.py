from django.shortcuts import render
from .models import Product
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