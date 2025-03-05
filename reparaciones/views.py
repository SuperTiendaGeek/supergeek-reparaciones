from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Para mostrar mensajes de error
from django.contrib.auth.decorators import login_required
from .models import OrdenReparacion, Cliente

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Intentando autenticar: {username} - {password}")  # Agregar depuración
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"Usuario autenticado: {user}")  # Agregar depuración
            return redirect('ordenes')
        else:
            print("Autenticación fallida")  # Agregar depuración
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'reparaciones/login.html')

@login_required
def ordenes_view(request):
    try:
        # Obtener la instancia del cliente basado en el usuario autenticado
        cliente = Cliente.objects.get(user=request.user)

        # Obtener las órdenes de reparación de ese cliente
        ordenes = OrdenReparacion.objects.filter(cliente=cliente)

        return render(request, 'ordenes.html', {'ordenes': ordenes})

    except Cliente.DoesNotExist:
        return render(request, 'ordenes.html', {'error': "No se encontró un cliente asociado a este usuario."})


@login_required
def ordenes_cliente(request):
    """Muestra las órdenes del cliente autenticado."""
    ordenes = OrdenReparacion.objects.filter(cliente__user=request.user)
    return render(request, 'ordenes.html', {'ordenes': ordenes})