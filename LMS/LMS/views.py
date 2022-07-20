from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect,render
from app.models import Categories,Course

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context = { 
        'category':category,
        'course':course,
    }
    return render(request,'Main/home.html',context)

def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category,

    }
    
    return render(request,'Main/single_course.html', context)

def CONTACT_US(request):
    return render(request,'Main/contact_us.html')

def ABOUT_US(request):
    return render(request,'Main/about_us.html')
