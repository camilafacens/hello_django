from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, val1, val2):
    val1 = 10
    val2 = 20
    return HttpResponse('Soma: {}'.format(val1+val2))