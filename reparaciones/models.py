from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import random
import string

# Modelo de usuario personalizado (Clientes)
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def generar_contrasena(self):
        """Genera una contraseña aleatoria de 8 caracteres."""
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))

    def save(self, *args, **kwargs):
        """Crear un usuario automáticamente cuando se registra un cliente nuevo."""
        if not self.user_id:  # Si el cliente no tiene usuario aún
            contrasena = self.generar_contrasena()
            usuario = User.objects.create_user(username=self.cedula, password=contrasena)
            self.user = usuario
            print(f"Contraseña generada para {self.cedula}: {contrasena}")  # Solo para debug

        super().save(*args, **kwargs)

# Modelo para las órdenes de reparación
class OrdenReparacion(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Reparado', 'Reparado')])
    item = models.CharField(max_length=255)
    problema = models.TextField()
    accesorios = models.TextField()
    fotos = models.ImageField(upload_to='ordenes_fotos/', blank=True, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        """Verifica si el cliente existe antes de guardar la orden."""
        if not self.cliente.user_id:  # Si el cliente no tiene usuario, lo crea
            self.cliente.save()  # Esto activará la creación automática de usuario
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden {self.codigo} - {self.item}"
    
class ActualizacionOrden(models.Model):
    orden = models.ForeignKey(OrdenReparacion, related_name="actualizaciones", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.orden.codigo} - {self.fecha}"
