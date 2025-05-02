from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Evento, RegistroEvento
from .forms import EventoForm, RegistroEventoForm
from django.contrib.auth.decorators import login_required

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user  # Asigna el usuario autenticado como organizador
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def registrar_en_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        # Verifica si el usuario ya está registrado
        registro, created = RegistroEvento.objects.get_or_create(usuario=request.user, evento=evento)
        if created:
            messages.success(request, f"Te has registrado exitosamente en el evento '{evento.nombre}'.")
        else:
            messages.warning(request, f"Ya estás registrado en el evento '{evento.nombre}'.")
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

def eliminar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})
