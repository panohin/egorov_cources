from django.shortcuts import render
from .models import Movie
from django.db.models import Sum, Max, Min, Avg

def show_all_movie(request):
    movies = Movie.objects.order_by('-rating')
    aggregate = movies.aggregate(Avg('rating'), Avg('budget'))
    context = {
        'movies' : movies,
        'aggregate' : aggregate
    }
    return render(request, 'movie_app/all_movies.html', context=context)

def show_one_movie(request, slug_movie: str):
    movie = Movie.objects.get(slug=slug_movie)
    return render(request, 'movie_app/one_movie.html',
        context={
                'movie' : movie
                })