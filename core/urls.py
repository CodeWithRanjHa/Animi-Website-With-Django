from django.urls import path
from .views import home, movie_detail, anime_watching, blog, categories, user_login, signup, categorie

urlpatterns = [
    path('', home, name='home'),
    path('movie_detail/<slug:slug>', movie_detail, name='movie_detail'),
    path('anime-watching/<slug:slug>', anime_watching, name='anime-watching'),
    path('blog/', blog, name='blog'),
    path('categorie/', categorie, name='categorie'),
    path('categories/<slug:slug>/', categories, name='categories'),
    path('login/', user_login, name='login'),
    path('signup/', signup, name='signup')
]
