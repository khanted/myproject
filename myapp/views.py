from django.shortcuts import render
from .models import Counter, Greeting
from django.http import HttpResponse
from datetime import datetime

# python manage.py runserver 8000

def stats(request):
    counter, created = Counter.objects.get_or_create(id=1)
    return render(request, 'myapp/index_stats.html', {'counter': counter})



def hello(request, name):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()

    gretting, created = Greeting.objects.get_or_create(name=name)
    last_greeting = Greeting.objects.last()

    gretting.greeting = str(last_greeting.timestamp)
    gretting.save()

    return render(request, 'myapp/index.html', {'name': name})


def grettings(request, name):
    greetings = Greeting.objects.filter(name=name)
    return render(request, 'myapp/index_stats_name.html', {'greetings': greetings, 'name': name})

    return HttpResponse(f"Hello, {name}! Last greeting was at {gretting.greeting}")
