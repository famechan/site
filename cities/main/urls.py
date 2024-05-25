from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.index, name='home'),

    path('brest', views.brest, name='brest'),
    path('kerch', views.kerch, name='kerch'),
    path('kiev', views.kiev, name='kiev'),
    path('leningrad', views.leningrad, name='leningrad'),
    path('minsk', views.minsk, name='minsk'),
    path('moscow', views.moscow, name='moscow'),
    path('murmansk', views.murmansk, name='murmansk'),
    path('novorossiysk', views.novorossiysk, name='novorossiysk'),
    path('odessa', views.odessa, name='odessa'),
    path('sevastopol', views.sevastopol, name='sevastopol'),
    path('smolensk', views.smolensk, name='smolensk'),
    path('stalingrad', views.stalingrad, name='stalingrad'),
    path('tula', views.tula, name='tula'),
]
