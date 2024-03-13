from django.shortcuts import render
import math 

def index(request):
    context = {"titulo":"Calculo del pago a Trabajadores",}
    return render(request, 'pagos/calcular_pago.html', context)

def enviar(request):
    if request.method == 'POST':
        pago_por_hora = float(request.POST.get('pago_por_hora'))
        horas_trabajadas = float(request.POST.get('horas_trabajadas'))
        pago_normal = min(40, horas_trabajadas) * pago_por_hora
        pago_extra = max(0, horas_trabajadas - 40) * (pago_por_hora * 2)
        pago_semanal = pago_normal + pago_extra
        
    context = {
        'titulo':"Respuesta",
        'pago_por_hora' : request.POST['pago_por_hora'],
        'horas_trabajadas' : request.POST['horas_trabajadas'],
        'pago_semanal' : pago_semanal,
        
    }
    return render(request, 'pagos/resultado.html', context )
