# clinica/serializers.py

# Bloque de Importaciones
# ======================================================================
from rest_framework import serializers # Importa la librería principal de serializadores de DRF
from .models import (
    Departamento, Especialidad, Paciente, Medico, Consulta_Medica,
    Tratamiento, Medicamento, Receta_Medica
) # Importa todos los modelos de la aplicación 'clinica'

# ----------------------------------------------------------------------
# SERIALIZADORES BÁSICOS: Uso de ModelSerializer para exponer modelos
# ----------------------------------------------------------------------
# ModelSerializer automatiza la creación de campos basada en los modelos
# de Django, facilitando la conversión de datos de Python a JSON y viceversa.

class DepartamentoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Departamento."""
    class Meta:
        model = Departamento
        fields = '__all__' # Incluye todos los campos del modelo en la API

class EspecialidadSerializer(serializers.ModelSerializer):
    """
    Serializador para Especialidad.
    Incluye un campo de solo lectura para mostrar el nombre del Departamento asociado.
    """
    # Campo personalizado: Muestra el campo 'nombre' del modelo 'departamento' relacionado
    # en lugar del ID (Foreign Key). Es 'read_only' para evitar que se envíe en la creación/actualización.
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True)
    class Meta:
        model = Especialidad
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Paciente."""
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    """
    Serializador para Médico.
    Incluye un campo de solo lectura para mostrar el nombre de la Especialidad.
    """
    # Campo personalizado: Muestra el campo 'nombre' del modelo 'especialidad' relacionado.
    especialidad_nombre = serializers.CharField(source='especialidad.nombre', read_only=True)
    class Meta:
        model = Medico
        fields = '__all__'

# Bloque de Serializadores con Campos Calculados (SerializerMethodField)
# ----------------------------------------------------------------------

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para Consulta Médica.
    Utiliza SerializerMethodField para crear campos que combinan datos,
    como el nombre completo del paciente y del médico.
    """
    # Campo calculado: El valor se obtiene llamando al método 'get_paciente_nombre_completo'.
    paciente_nombre_completo = serializers.SerializerMethodField()
    # Campo calculado: El valor se obtiene llamando al método 'get_medico_nombre_completo'.
    medico_nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Consulta_Medica
        fields = '__all__'

    # Implementación del método para obtener el nombre completo del paciente.
    def get_paciente_nombre_completo(self, obj):
        """Combina el nombre y apellido del paciente asociado."""
        return f"{obj.paciente.nombre} {obj.paciente.apellido}"

    # Implementación del método para obtener el nombre completo del médico.
    def get_medico_nombre_completo(self, obj):
        """Combina el nombre y apellido del médico asociado."""
        return f"{obj.medico.nombre} {obj.medico.apellido}"

# Bloque de Serializadores Adicionales
# ----------------------------------------------------------------------

class TratamientoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Tratamiento."""
    class Meta:
        model = Tratamiento
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Medicamento."""
    class Meta:
        model = Medicamento
        fields = '__all__'

class RecetaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para Receta Médica.
    Incluye el nombre del Medicamento asociado en lugar de solo su ID.
    """
    # Campo personalizado: Muestra el campo 'nombre' del modelo 'medicamento' relacionado.
    medicamento_nombre = serializers.CharField(source='medicamento.nombre', read_only=True)
    class Meta:
        model = Receta_Medica
        fields = '__all__'