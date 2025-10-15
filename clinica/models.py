from django.db import models

# Create your models here.
# clinica/models.py
from django.db import models
from django.core.validators import MinValueValidator
from datetime import date
from decimal import Decimal

#
"""
Módulo de Modelos de Datos para Salud Vital 
Incluye las 7 entidades principales (Especialidad, Paciente, Médico,
Consulta_Medica, Tratamiento, Medicamento, Receta_Medica),
la mejora de la tabla 'Departamento' y CHOICES para 'estado'.
"""

# ----------------------------------------------------------------------
# MEJORA: Nueva Tabla Adicional: Departamento
# ----------------------------------------------------------------------
class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    # FK a Departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.CharField(max_length=5, help_text="Ej: A+, O-")
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

class Medico(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    activo = models.BooleanField(default=True)
    # FK a Especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

# ----------------------------------------------------------------------
# MEJORA: Uso de CHOICES para el campo 'estado' en Consulta_Medica
# ----------------------------------------------------------------------
ESTADO_CONSULTA_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
]

class Consulta_Medica(models.Model):
    # FKs
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    
    fecha_consulta = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=255)
    diagnostico = models.TextField(blank=True, null=True)
    # Uso del CHOICES definido
    estado = models.CharField(max_length=20, choices=ESTADO_CONSULTA_CHOICES, default='PENDIENTE')

    class Meta:
        verbose_name_plural = "Consultas Médicas"
        ordering = ['-fecha_consulta']

    def __str__(self):
        return f"Consulta {self.id} de {self.paciente}"

class Tratamiento(models.Model):
    # FK a Consulta_Medica
    consulta = models.ForeignKey(Consulta_Medica, on_delete=models.CASCADE)
    
    descripcion = models.TextField()
    duracion_dias = models.IntegerField(validators=[MinValueValidator(1)])
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Tratamiento {self.id} para Consulta {self.consulta.id}"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio})"

class Receta_Medica(models.Model):
    # FKs
    consulta = models.ForeignKey(Consulta_Medica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    
    dosis = models.CharField(max_length=150)
    frecuencia = models.CharField(max_length=150)
    duracion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Recetas Médicas"

    def __str__(self):
        return f"Receta para {self.consulta.paciente} - {self.medicamento.nombre}"

