from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index (request):
    return HttpResponse ("Страница приложения films")


def categories (request, genre_id):
    return HttpResponse (f"<h1>Категории</h1><p>id: {genre_id}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h2>")
