from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la vista Calculadora")

def suma(request, numero1,numero2):
    sum = numero1 + numero2
    return HttpResponse("La suma de %s + %s = %s." %(numero1, numero2, sum))

def resta(request, numero1,numero2):
    rest = numero1 - numero2
    return HttpResponse("La resta de %s - %s = %s." %(numero1, numero2, rest))

def multiplicacion(request, numero1,numero2):
    mult = numero1 * numero2
    return HttpResponse("La multiplicacion de %s * %s = %s." %(numero1, numero2, mult))

def division(request, numero1,numero2):
    div = numero1 / numero2
    return HttpResponse("La division de %s / %s = %s." %(numero1, numero2, div))




