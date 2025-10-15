# Bloque de Importaciones y Dependencias
# ======================================================================
import django_filters # Se importa la librería principal para crear filtros dinámicos basados en modelos.
from .models import (
    Departamento, Especialidad, Paciente, Medico, Consulta_Medica,
    Tratamiento, Medicamento, Receta_Medica
) # Se importan todos los modelos que serán utilizados como fuente de datos para los filtros.

# ======================================================================
# DEFINICIÓN DE CLASES FILTERSET POR ENTIDAD
# Cada clase FilterSet crea un formulario de filtrado que permite consultar
# el QuerySet de un modelo específico mediante la URL (parámetros GET).
# ======================================================================

# ----------------- 1. Departamento Filter -----------------
class DepartamentoFilter(django_filters.FilterSet):
    """
    Define el filtro para la entidad Departamento. Permite buscar por el campo 'nombre'
    utilizando una coincidencia de texto parcial e insensible a mayúsculas/minúsculas ('icontains').
    """
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Buscar por Nombre')

    class Meta:
        model = Departamento
        fields = ['nombre']

# ----------------- 2. Especialidad Filter -----------------
class EspecialidadFilter(django_filters.FilterSet):
    """
    Define el filtro para Especialidad. Permite la búsqueda de texto por 'nombre'
    y ofrece un selector de lista para filtrar por el Departamento asociado (FK).
    """
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Buscar por Nombre')
    
    class Meta:
        model = Especialidad
        fields = ['nombre', 'departamento'] 

# ----------------- 3. Paciente Filter -----------------
class PacienteFilter(django_filters.FilterSet):
    """
    Define el filtro para Paciente. Permite la búsqueda de texto por 'nombre' y 'rut'.
    También incluye el campo booleano 'activo' para filtrar por el estado del paciente.
    """
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre/Apellido')
    rut = django_filters.CharFilter(lookup_expr='icontains', label='RUT')

    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'activo']

# ----------------- 4. Medico Filter -----------------
class MedicoFilter(django_filters.FilterSet):
    """
    Define el filtro para Médico. Permite buscar por texto ('nombre', 'rut') y
    filtrar por la 'especialidad' asociada y el estado 'activo' (booleano).
    """
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre/Apellido')
    rut = django_filters.CharFilter(lookup_expr='icontains', label='RUT')

    class Meta:
        model = Medico
        fields = ['rut', 'nombre', 'especialidad', 'activo'] 

# ----------------- 5. Consulta_Medica Filter -----------------
class ConsultaMedicaFilter(django_filters.FilterSet):
    """
    Define el filtro para Consulta_Medica. Incluye filtros de rango temporal
    ('fecha_consulta_min' y 'fecha_consulta_max') y selectores para las
    llaves foráneas ('paciente', 'medico') y el campo de opciones ('estado').
    """
    # Filtros de fecha_consulta para rangos (mayor/menor o igual)
    fecha_consulta_min = django_filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='gte', label='Fecha Desde')
    fecha_consulta_max = django_filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='lte', label='Fecha Hasta')
    
    class Meta:
        model = Consulta_Medica
        fields = ['paciente', 'medico', 'estado'] 

# ----------------- 6. Tratamiento Filter -----------------
class TratamientoFilter(django_filters.FilterSet):
    """
    Define el filtro para Tratamiento. Permite buscar por texto en la 'descripcion'
    y filtrar por la 'consulta' médica a la que está asociado el tratamiento.
    """
    descripcion = django_filters.CharFilter(lookup_expr='icontains', label='Descripción')
    
    class Meta:
        model = Tratamiento
        fields = ['consulta', 'descripcion']

# ----------------- 7. Medicamento Filter -----------------
class MedicamentoFilter(django_filters.FilterSet):
    """
    Define el filtro para Medicamento. Permite buscar por el 'nombre' y el
    'laboratorio' utilizando búsqueda de texto parcial.
    """
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
    laboratorio = django_filters.CharFilter(lookup_expr='icontains', label='Laboratorio')
    
    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio']

# ----------------- 8. Receta_Medica Filter -----------------
class RecetaMedicaFilter(django_filters.FilterSet):
    """
    Define el filtro para Receta_Medica. Permite la búsqueda de texto en la 'dosis'
    y filtrar por las llaves foráneas 'consulta' y 'medicamento'.
    """
    dosis = django_filters.CharFilter(lookup_expr='icontains', label='Dosis')

    class Meta:
        model = Receta_Medica
        fields = ['consulta', 'medicamento']