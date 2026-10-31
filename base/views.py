from django.shortcuts import render

# Create your views here.

def home(request):


    fruits = ['apple', 'cherry', 'bannana', 'orange']


    context = {
        'age' : 12,
        'name' : 'john',
        'isLogin' : False,
        'MyList' : fruits,
    }
    return render(request, 'index.html', context)

