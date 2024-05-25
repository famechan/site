from django.shortcuts import render

def index (request):
    return render(request, 'main/index.html')
def brest(request):
    return render(request, 'main/heroic-cities/brest.html')
def kerch(request):
    return render(request, 'main/heroic-cities/kerch.html')
def kiev(request):
    return render(request, 'main/heroic-cities/kiev.html')
def leningrad(request):
    return render(request, 'main/heroic-cities/leningrad.html')
def minsk(request):
    return render(request, 'main/heroic-cities/minsk.html')
def moscow(request):
    return render(request, 'main/heroic-cities/moscow.html')
def murmansk(request):
    return render(request, 'main/heroic-cities/murmansk.html')
def novorossiysk(request):
    return render(request, 'main/heroic-cities/novorossiysk.html')
def odessa(request):
    return render(request, 'main/heroic-cities/odessa.html')
def sevastopol(request):
    return render(request, 'main/heroic-cities/sevastopol.html')
def smolensk(request):
    return render(request, 'main/heroic-cities/smolensk.html')
def stalingrad(request):
    return render(request, 'main/heroic-cities/stalingrad.html')
def tula(request):
    return render(request, 'main/heroic-cities/tula.html')

