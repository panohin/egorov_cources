from curses.ascii import HT
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


days_of_week_list = ['monday', 'tuesday', 'wednesday', 'thursday',
                                    'friday', 'saturday','sunday']

def index(request):
    context = {
        "days_of_week_list" : days_of_week_list
    }
    return render(request, 'todo_week/greeting.html', context=context)
    
def get_todo_list_on_day(request, name_of_day):
    context = {
        'name_of_day' : name_of_day
    }
    if name_of_day.lower() in days_of_week_list:
        return render(request, 'todo_week/week_day.html', context=context)
    else:
        return HttpResponse(f"{name_of_day} is not a day of the week")

def get_todo_list_on_day_by_number(request, name_of_day: int):
    if name_of_day in range(1,8):
        name_of_day = days_of_week_list[name_of_day - 1]
        redirect_url = reverse("name_of_day_url", args=(name_of_day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse(f"Неверный номер дня - {name_of_day}")
