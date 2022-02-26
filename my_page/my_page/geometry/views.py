from math import pi
from turtle import width
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def get_circle_area(request, radius: int):
    square = pi * radius * radius
    return render(request, 'geometry/circle.html')
    # if square > 0:
    #     return HttpResponse(f"Площадь круга с радиусом {radius} равна {square}")
    # else:
    #     return HttpResponse(f"Значения {radius} введены с ошибкой")

    
def get_square_area(request, width: int):
    square = width * width
    return render(request, 'geometry/square.html')
    # if square > 0:
    #     return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {square}")
    # else:
    #     return HttpResponse(f"Значения {width} введены с ошибкой")


def get_rectangle_area(request, width: int, height: int):
    square = width * height
    return render(request, 'geometry/rectangle.html')
    # if square > 0:
    #     return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {square}")
    # else:
    #     return HttpResponse(f"Значения {width} и {height} введены с ошибкой")
    
