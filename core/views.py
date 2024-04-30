from django.shortcuts import render, redirect
from .models import Movie, Banners, Side_items
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User



def home(request):
    banners = Banners.objects.all()
    most_popular = Movie.objects.filter(status='MP')
    trending_now = Movie.objects.filter(status='TN')
    side_items = Side_items.objects.all()

    context ={
        'most_popular': most_popular,
        'trending_now': trending_now,
        'banners': banners, 
        'side_items': side_items,
    }
    return render(request, 'index.html', context)



def movie_detail(request, slug):
    movie = Movie.objects.get(new_slug=slug)
    side_items = Side_items.objects.all()
    context ={
        'movie': movie,
        'side_items': side_items,
    }
    return render(request, 'anime-details.html', context)



def anime_watching(request, slug):
    movie = Movie.objects.get(new_slug=slug)

    context = {
        'movie':movie
    }
    return render(request, 'anime-watching.html', context)


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def main_page(request):
    return render(request, 'main.html')


def categories(request):
    return render(request, 'categories.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            redirect('home')
            

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if email and password and name:
            user = User.objects.create_user(email, password=password, username=name)
            user.save()
            redirect('home')
    return render(request, 'signup.html')