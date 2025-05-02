from django import forms
from .models import Evento, RegistroEvento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'lugar', 'capacidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-gray-900 text-white placeholder-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Nombre del evento'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-3 bg-gray-900 text-white placeholder-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Descripción del evento'
            }),
            'fecha': forms.DateTimeInput(attrs={
                'class': 'w-full p-3 bg-gray-900 text-white placeholder-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'YYYY-MM-DD HH:MM:SS',
                'type': 'datetime-local' 
            }),
            'lugar': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-gray-900 text-white placeholder-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Lugar del evento'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'w-full p-3 bg-gray-900 text-white placeholder-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Capacidad máxima'
            }),
        }

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = []