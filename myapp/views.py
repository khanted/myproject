from django.shortcuts import render
from .models import Counter, Greeting
from django.http import HttpResponse
from datetime import datetime

# python manage.py runserver 8000

def stats(request):
    counter, created = Counter.objects.get_or_create(id=1)
    return HttpResponse(f"Всего приветствий было: {counter.count}.")


def hello(request, name):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()

    gretting, created = Greeting.objects.get_or_create(name=name)
    last_greeting = Greeting.objects.last()

    gretting.greeting = str(last_greeting.timestamp)
    gretting.save()

    return HttpResponse(f"Hello, {name}!")


def grettings(request, name):
    gretting, created = Greeting.objects.get_or_create(name=name)

    return HttpResponse(f"Hello, {name}! Last greeting was at {gretting.greeting}")
