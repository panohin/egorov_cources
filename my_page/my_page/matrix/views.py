from django.shortcuts import render


def index(request):
    data = {
        'year_born' : 1980,
        'city_born' : 'Мельбурн',
        'movie_name' : 'Матрица',

    }
    return render(request, 'matrix/matrix.html', context=data)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'matrix/guinnessworldrecords.html', context=context)
