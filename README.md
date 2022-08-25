# egorov_cources

Django проекты по курсу Егорова Артёма:
https://www.youtube.com/watch?v=DYxjL0K3Hwk&list=PLQAt0m1f9OHvGM7Y7jAQP8TKbBd3up4K2

Технологии:
- templates
- slug
- queryset
- get_absolute_url
- static (css)

1. bookshop
Только создано приложение bookapp
2. movie_proj
Приложение со списком фильмов, их наименованием, рейтингом, годом выхода и бюджетом.
На главной выводится список, средний рейтинг и средний бюджет. Отдельные страницы для каждой картины. 
3. my_page
Несколько приложений: horoscope - список знаков зодиака, индивидуальная страница для каждого знака, возможность определить знак по дате (url-запрос: /horoscope/<month>/<day>);
geometry - подсчёт площади геометрической фигуры (calculate_geometry/rectangle/<int:width>/<int:height>, square/<int:width>, circle/<int:radius>); matrix - что-то непонятное :-).
4. week_days
Список дней недели и отдельная страница для каждого дня. Примитивно.
