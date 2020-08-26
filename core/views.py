from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, val1, val2):
    return HttpResponse('Soma: {}'.format(val1+val2))

def multiplicacao (request, val1, val2):
    return HttpResponse('Multiplicacao: {}'.format(val1 * val2))