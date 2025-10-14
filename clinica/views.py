# Bloque de Importaciones Estándar de Django y Librerías Externas
# ======================================================================
from django.shortcuts import render # Función básica no usada, pero estándar
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # Vistas basadas en clase para CRUD
from django.urls import reverse_lazy # Permite hacer redirecciones sin cargar la URL hasta que sea necesaria
from rest_framework import viewsets # Provee las clases para crear endpoints de API REST
from django_filters.rest_framework import DjangoFilterBackend # Backend para habilitar filtrado en las APIs

# Bloque de Importaciones Locales de la Aplicación 'clinica'
# ======================================================================
from .models import (
    Departamento, Especialidad, Paciente, Medico, Consulta_Medica,
    Tratamiento, Medicamento, Receta_Medica
) # Importación de todos los modelos de la base de datos
from .forms import (
    DepartamentoForm, EspecialidadForm, PacienteForm, MedicoForm, ConsultaMedicaForm,
    TratamientoForm, MedicamentoForm, RecetaMedicaForm
) # Importación de los formularios para las vistas Create/Update
from .serializers import (
    DepartamentoSerializer, EspecialidadSerializer, PacienteSerializer, MedicoSerializer, ConsultaMedicaSerializer,
    TratamientoSerializer, MedicamentoSerializer, RecetaMedicaSerializer
) # Importación de los serializadores para las vistas de la API (DRF)
from .filters import (
    DepartamentoFilter, EspecialidadFilter, PacienteFilter, MedicoFilter, ConsultaMedicaFilter,
    TratamientoFilter, MedicamentoFilter, RecetaMedicaFilter
) # Importación de los filtros (django-filters) para búsquedas en vistas HTML y la API

# ======================================================================
# VISTAS BASADAS EN TEMPLATES (CRUD HTML) - LÓGICA DE FILTRADO
# ======================================================================

# --- Mixin para Filtrado y Ordenamiento ---
class FilteredListViewMixin:
    """
    Mixin para aplicar filtros de django-filters y ordenamiento (sorting)
    a cualquier vista ListView que herede de él.
    """
    filterset_class = None # Se debe definir la clase FilterSet específica en la subclase
    
    def get_queryset(self):
        """
        Sobrescribe el queryset base para aplicar el filtrado y ordenamiento 
        basado en los parámetros GET de la solicitud (URL).
        """
        queryset = super().get_queryset()
        
        # 1. Aplicar Filtrado (Search)
        # Crea una instancia del filtro usando los parámetros de la URL (self.request.GET)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs # Obtiene el queryset filtrado
        
        # 2. Aplicar Ordenamiento (Sorting)
        ordering = self.request.GET.get('ordering', None)
        if ordering:
            queryset = queryset.order_by(ordering)
            
        return queryset

# ======================================================================
# VISTAS BASADAS EN TEMPLATES (CRUD HTML) - IMPLEMENTACIÓN POR ENTIDAD
# ======================================================================

# 1. Departamento (CRUD completo)
class DepartamentoListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Departamentos con soporte para filtrado."""
    model = Departamento
    template_name = 'clinica/departamento_list.html'
    context_object_name = 'object_list' # Nombre de la variable que contendrá los datos en el template
    filterset_class = DepartamentoFilter # Clase de filtro específica para esta lista
class DepartamentoCreateView(CreateView):
    """Permite crear un nuevo Departamento."""
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'clinica/_form_generico.html' # Template genérico para formularios
    success_url = reverse_lazy('departamento-list') # Redirección después de una creación exitosa
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Departamento'
        context['cancel_url'] = reverse_lazy('departamento-list')
        return context
class DepartamentoUpdateView(UpdateView):
    """Permite editar un Departamento existente."""
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'clinica/_form_generico.html' # Template genérico para formularios
    success_url = reverse_lazy('departamento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Departamento'
        context['cancel_url'] = reverse_lazy('departamento-list')
        return context
class DepartamentoDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina un Departamento."""
    model = Departamento
    template_name = 'clinica/_confirm_delete.html' # Template genérico para confirmación de borrado
    success_url = reverse_lazy('departamento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Departamento'
        context['cancel_url'] = reverse_lazy('departamento-list')
        return context

# 2. Especialidad (CRUD completo, sigue el mismo patrón que Departamento)
class EspecialidadListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Especialidades con soporte para filtrado."""
    model = Especialidad
    template_name = 'clinica/especialidad_list.html'
    context_object_name = 'object_list'
    filterset_class = EspecialidadFilter
class EspecialidadCreateView(CreateView):
    """Permite crear una nueva Especialidad."""
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('especialidad-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Especialidad'
        context['cancel_url'] = reverse_lazy('especialidad-list')
        return context
class EspecialidadUpdateView(UpdateView):
    """Permite editar una Especialidad existente."""
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('especialidad-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Especialidad'
        context['cancel_url'] = reverse_lazy('especialidad-list')
        return context
class EspecialidadDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina una Especialidad."""
    model = Especialidad
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('especialidad-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Especialidad'
        context['cancel_url'] = reverse_lazy('especialidad-list')
        return context

# 3. Paciente (CRUD completo, sigue el mismo patrón)
class PacienteListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Pacientes con soporte para filtrado."""
    model = Paciente
    template_name = 'clinica/paciente_list.html'
    context_object_name = 'object_list'
    filterset_class = PacienteFilter
class PacienteCreateView(CreateView):
    """Permite crear un nuevo Paciente."""
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('paciente-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Paciente'
        context['cancel_url'] = reverse_lazy('paciente-list')
        return context
class PacienteUpdateView(UpdateView):
    """Permite editar un Paciente existente."""
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('paciente-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Paciente'
        context['cancel_url'] = reverse_lazy('paciente-list')
        return context
class PacienteDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina un Paciente."""
    model = Paciente
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('paciente-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Paciente'
        context['cancel_url'] = reverse_lazy('paciente-list')
        return context

# 4. Medico (CRUD completo, sigue el mismo patrón)
class MedicoListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Médicos con soporte para filtrado."""
    model = Medico
    template_name = 'clinica/medico_list.html'
    context_object_name = 'object_list'
    filterset_class = MedicoFilter
class MedicoCreateView(CreateView):
    """Permite crear un nuevo Médico."""
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('medico-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Médico'
        context['cancel_url'] = reverse_lazy('medico-list')
        return context
class MedicoUpdateView(UpdateView):
    """Permite editar un Médico existente."""
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('medico-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Médico'
        context['cancel_url'] = reverse_lazy('medico-list')
        return context
class MedicoDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina un Médico."""
    model = Medico
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('medico-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Médico'
        context['cancel_url'] = reverse_lazy('medico-list')
        return context

# 5. Consulta_Medica (CRUD completo, sigue el mismo patrón)
class ConsultaMedicaListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Consultas Médicas con soporte para filtrado."""
    model = Consulta_Medica
    template_name = 'clinica/consultamedica_list.html'
    context_object_name = 'object_list'
    filterset_class = ConsultaMedicaFilter
class ConsultaMedicaCreateView(CreateView):
    """Permite crear una nueva Consulta Médica."""
    model = Consulta_Medica
    form_class = ConsultaMedicaForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('consultamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Consulta Médica'
        context['cancel_url'] = reverse_lazy('consultamedica-list')
        return context
class ConsultaMedicaUpdateView(UpdateView):
    """Permite editar una Consulta Médica existente."""
    model = Consulta_Medica
    form_class = ConsultaMedicaForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('consultamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Consulta Médica'
        context['cancel_url'] = reverse_lazy('consultamedica-list')
        return context
class ConsultaMedicaDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina una Consulta Médica."""
    model = Consulta_Medica
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('consultamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Consulta Médica'
        context['cancel_url'] = reverse_lazy('consultamedica-list')
        return context

# 6. Tratamiento (CRUD completo, sigue el mismo patrón)
class TratamientoListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Tratamientos con soporte para filtrado."""
    model = Tratamiento
    template_name = 'clinica/tratamiento_list.html'
    context_object_name = 'object_list'
    filterset_class = TratamientoFilter
class TratamientoCreateView(CreateView):
    """Permite crear un nuevo Tratamiento."""
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('tratamiento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tratamiento'
        context['cancel_url'] = reverse_lazy('tratamiento-list')
        return context
class TratamientoUpdateView(UpdateView):
    """Permite editar un Tratamiento existente."""
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('tratamiento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tratamiento'
        context['cancel_url'] = reverse_lazy('tratamiento-list')
        return context
class TratamientoDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina un Tratamiento."""
    model = Tratamiento
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('tratamiento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tratamiento'
        context['cancel_url'] = reverse_lazy('tratamiento-list')
        return context

# 7. Medicamento (CRUD completo, sigue el mismo patrón)
class MedicamentoListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Medicamentos con soporte para filtrado."""
    model = Medicamento
    template_name = 'clinica/medicamento_list.html'
    context_object_name = 'object_list'
    filterset_class = MedicamentoFilter
class MedicamentoCreateView(CreateView):
    """Permite crear un nuevo Medicamento."""
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('medicamento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicamento'
        context['cancel_url'] = reverse_lazy('medicamento-list')
        return context
class MedicamentoUpdateView(UpdateView):
    """Permite editar un Medicamento existente."""
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('medicamento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicamento'
        context['cancel_url'] = reverse_lazy('medicamento-list')
        return context
class MedicamentoDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina un Medicamento."""
    model = Medicamento
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('medicamento-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicamento'
        context['cancel_url'] = reverse_lazy('medicamento-list')
        return context

# 8. Receta_Medica (CRUD completo, sigue el mismo patrón)
class RecetaMedicaListView(FilteredListViewMixin, ListView):
    """Muestra una lista de Recetas Médicas con soporte para filtrado."""
    model = Receta_Medica
    template_name = 'clinica/recetamedica_list.html'
    context_object_name = 'object_list'
    filterset_class = RecetaMedicaFilter
class RecetaMedicaCreateView(CreateView):
    """Permite crear una nueva Receta Médica."""
    model = Receta_Medica
    form_class = RecetaMedicaForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('recetamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Receta Médica'
        context['cancel_url'] = reverse_lazy('recetamedica-list')
        return context
class RecetaMedicaUpdateView(UpdateView):
    """Permite editar una Receta Médica existente."""
    model = Receta_Medica
    form_class = RecetaMedicaForm
    template_name = 'clinica/_form_generico.html'
    success_url = reverse_lazy('recetamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Receta Médica'
        context['cancel_url'] = reverse_lazy('recetamedica-list')
        return context
class RecetaMedicaDeleteView(DeleteView):
    """Muestra una página de confirmación y elimina una Receta Médica."""
    model = Receta_Medica
    template_name = 'clinica/_confirm_delete.html'
    success_url = reverse_lazy('recetamedica-list')
    def get_context_data(self, **kwargs):
        """Añade el nombre del modelo y la URL de cancelación al contexto."""
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Receta Médica'
        context['cancel_url'] = reverse_lazy('recetamedica-list')
        return context

# ======================================================================
# VISTAS DE LA API (ViewSets)
# ======================================================================

# Implementación de ViewSets (API REST) para cada modelo.
# ModelViewSet provee automáticamente las operaciones CRUD (list, create, retrieve, update, destroy).

class DepartamentoViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Departamentos."""
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Especialidades."""
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Pacientes, con soporte para filtrado."""
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend] # Habilita el backend de filtrado
    filterset_class = PacienteFilter # Clase de filtro para este ViewSet

class MedicoViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Médicos, con soporte para filtrado."""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MedicoFilter

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Consultas Médicas, con soporte para filtrado."""
    queryset = Consulta_Medica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultaMedicaFilter

class TratamientoViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Tratamientos."""
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Medicamentos."""
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    """Endpoint de la API para la gestión de Recetas Médicas."""
    queryset = Receta_Medica.objects.all()
    serializer_class = RecetaMedicaSerializer

