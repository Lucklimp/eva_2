# Bloque de Importaciones
# ======================================================================
from django import forms # Módulo base para la creación de formularios en Django
from .models import (
    Departamento, Especialidad, Paciente, Medico, Consulta_Medica,
    Tratamiento, Medicamento, Receta_Medica
) # Importación de todos los modelos de la aplicación 'clinica'
from crispy_forms.helper import FormHelper # Clase principal para la personalización de formularios con crispy-forms
from crispy_forms.layout import Layout, Submit # Clases para definir la estructura y elementos de envío (botones)

# ======================================================================
# FORMULARIOS MODELFORM (CRUD HTML)
# Todos los formularios usan FormHelper para aplicar estilos (ej: Bootstrap)
# y añadir automáticamente un botón de "Guardar".
# ======================================================================

class DepartamentoForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Departamento."""
    class Meta:
        model = Departamento
        fields = '__all__' # Incluye todos los campos del modelo
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper() # Inicializa la ayuda de crispy-forms
        # Añade el botón de envío (Submit) con texto y clase CSS
        self.helper.add_input(Submit('submit', 'Guardar Departamento', css_class='btn-primary'))

class EspecialidadForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Especialidad."""
    class Meta:
        model = Especialidad
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Especialidad', css_class='btn-primary'))

class PacienteForm(forms.ModelForm):
    """
    Formulario ModelForm para la entidad Paciente.
    Personaliza el widget de fecha de nacimiento.
    """
    class Meta:
        model = Paciente
        fields = '__all__'
        # Configuración de widget: Asegura que la entrada de fecha se muestre como un selector de calendario HTML5
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Paciente', css_class='btn-primary'))

class MedicoForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Medico."""
    class Meta:
        model = Medico
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Médico', css_class='btn-primary'))

class ConsultaMedicaForm(forms.ModelForm):
    """
    Formulario ModelForm para la entidad Consulta_Medica.
    Define explícitamente los campos que se desean utilizar.
    """
    class Meta:
        model = Consulta_Medica
        # Lista de campos específicos incluidos en este formulario
        fields = ['paciente', 'medico', 'motivo', 'diagnostico', 'estado'] #vhoices

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Consulta', css_class='btn-primary'))

class TratamientoForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Tratamiento."""
    class Meta:
        model = Tratamiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Tratamiento', css_class='btn-primary'))

class MedicamentoForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Medicamento."""
    class Meta:
        model = Medicamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Medicamento', css_class='btn-primary'))

class RecetaMedicaForm(forms.ModelForm):
    """Formulario ModelForm para la entidad Receta_Medica."""
    class Meta:
        model = Receta_Medica
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar Receta', css_class='btn-primary'))