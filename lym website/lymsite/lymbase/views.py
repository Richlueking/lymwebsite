from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    activities = Activity.objects.all()[0:5]
    context = {'activities': activities}
    return render(request, 'lymbase/home.html', context)


def service(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'lymbase/service.html', context)


def team(request):
    members = Team.objects.all()
    context = {'members': members}
    return render(request, 'lymbase/team.html', context)


def activity(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'lymbase/activities.html', context)


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'lymbase/blogs.html', context)


def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'lymbase/blog_detail.html', context)
