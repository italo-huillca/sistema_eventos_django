from django.shortcuts import render, redirect
from .models import Evento, RegistroEvento
from .forms import EventoForm, RegistroEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})
def registrar_en_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    if request.method == 'POST':
        registro, created = RegistroEvento.objects.get_or_create(usuario=request.user, evento=evento)
        return redirect('detalle_evento', evento_id=evento_id)
    return render(request, 'eventos/registrar_en_evento.html', {'evento': evento})
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    registros = RegistroEvento.objects.filter(evento=evento)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'registros': registros})
def editar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form})
