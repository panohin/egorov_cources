from datetime import date
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


zodiac_dates_dict = {
                    'aries': [range(321,332), range(401,421)],
                    'taurus': [range(421,431), range(501,522)],
                    'gemini': [range(522,532), range(601,622)],
                    'cancer': [range(622,631), range(701,723)],
                    'leo': [range(723,732), range(801,822)],
                    'virgo': [range(822,832), range(901,924)],
                    'libra': [range(924,931), range(1001,1024)], 
                    'scorpio': [range(1024,1032), range(1101,1123)],
                    'sagittarius': [range(1123,1131), range(1201,1223)],
                    'capricorn': [range(1223,1232), range(101,121)],
                    'aquarius': [range(121,132), range(201,220)],
                    'pisces': [range(220,230), range(301,321)]
}

zodiac_info_dict = {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
                    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
                    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
                    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
                    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
                    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
                    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
                    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
                    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
                    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
                    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
                    }

types_of_zodiac_signs_dict = {
    "fire" : ['aries', 'leo', 'sagittarius'],
    "earth" : ['taurus', 'virgo', 'capricorn'],
    "air" : ['gemini', 'libra', 'aquarius'],
    "water" : ['cancer', 'scorpio', 'pisces']
}


def index(request):
    context = {
        "zodiac_dates_dict" : zodiac_dates_dict
    }
    return render(request, 'horoscope/index.html', context=context)


def info_about_zodiac_sign(request, zodiac_sign):
    description = zodiac_info_dict.get(zodiac_sign)
    data = {
        "description_zodiac" : description,
        "sign" : zodiac_sign,
        "value" : []
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)
    

       
def info_about_zodiac_sign_by_number(request, zodiac_sign: int):
    if zodiac_sign < 1 or zodiac_sign > len(zodiac_info_dict):
        return HttpResponse(f"{zodiac_sign} is not a number of zodiac sign")
    else:
        zodiac_info_key = list(zodiac_info_dict)[zodiac_sign - 1]
        redirect_url = reverse("horoscope_URL", args=(zodiac_info_key, ))
        return HttpResponseRedirect(redirect_url) 

def list_of_types(request):
    response = ''
    for type in types_of_zodiac_signs_dict:
        redirect_path = reverse("zodiac_type_url", args=(type, ))
        response += f'<li><a href={redirect_path}><font size="5">{type}</a></li>'
    return HttpResponse(response)

def sighs_by_type(request, zodiac_type):
    response = ''
    for zodiac_sign in types_of_zodiac_signs_dict[zodiac_type]:
        redirect_url = reverse("horoscope_URL", args=(zodiac_sign, ))
        response += f"<li><a href={redirect_url}>{zodiac_sign}</a></li>"
    return HttpResponse(response)

def get_info_by_date(request, month:int, day: int):
    if len(str(day)) == 1:
        day = "0" + str(day)
    date_alias = int(str(month) + str(day))
    
    for zodiac_name in zodiac_dates_dict:
        for interval in zodiac_dates_dict[zodiac_name]:
            if date_alias in interval:
                redirect_url = reverse("horoscope_URL", args=(zodiac_name, ))
                return HttpResponse(f"Введённая дата: месяц {month}, день {day}<br><br><font size='5'>Знак зодиака: <a href={redirect_url}>{zodiac_name}</a>")
    return HttpResponse('error')
    