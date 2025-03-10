from django.urls import path
from myapp import views


urlpatterns = [
    path('hello/<str:name>/', views.hello, name='hello'),
    path('stats/', views.stats, name='stats'),
    path('stats/<str:name>/', views.grettings, name='greetings'),
]
