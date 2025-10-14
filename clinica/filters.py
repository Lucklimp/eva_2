# clinica/filters.py

import django_filters
from .models import (
    Departamento, Especialidad, Paciente, Medico, Consulta_Medica,
    Tratamiento, Medicamento, Receta_Medica
)

# ----------------- 1. Departamento Filter -----------------
class DepartamentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Buscar por Nombre')

    class Meta:
        model = Departamento
        fields = ['nombre']

# ----------------- 2. Especialidad Filter -----------------
class EspecialidadFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Buscar por Nombre')
    
    class Meta:
        model = Especialidad
        fields = ['nombre', 'departamento'] 

# ----------------- 3. Paciente Filter -----------------
class PacienteFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre/Apellido')
    rut = django_filters.CharFilter(lookup_expr='icontains', label='RUT')

    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'activo']

# ----------------- 4. Medico Filter -----------------
class MedicoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre/Apellido')
    rut = django_filters.CharFilter(lookup_expr='icontains', label='RUT')

    class Meta:
        model = Medico
        fields = ['rut', 'nombre', 'especialidad', 'activo'] 

# ----------------- 5. Consulta_Medica Filter -----------------
class ConsultaMedicaFilter(django_filters.FilterSet):
    # Permite filtrar por rango de fecha
    fecha_consulta_min = django_filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='gte', label='Fecha Desde')
    fecha_consulta_max = django_filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='lte', label='Fecha Hasta')
    
    class Meta:
        model = Consulta_Medica
        fields = ['paciente', 'medico', 'estado'] # Filtrar por FKs y CHOICES

# ----------------- 6. Tratamiento Filter -----------------
class TratamientoFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='icontains', label='Descripción')
    
    class Meta:
        model = Tratamiento
        fields = ['consulta', 'descripcion']

# ----------------- 7. Medicamento Filter -----------------
class MedicamentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
    laboratorio = django_filters.CharFilter(lookup_expr='icontains', label='Laboratorio')
    
    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio']

# ----------------- 8. Receta_Medica Filter -----------------
class RecetaMedicaFilter(django_filters.FilterSet):
    dosis = django_filters.CharFilter(lookup_expr='icontains', label='Dosis')

    class Meta:
        model = Receta_Medica
        fields = ['consulta', 'medicamento']