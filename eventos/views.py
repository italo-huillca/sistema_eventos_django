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
