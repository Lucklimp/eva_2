# clinica/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # Importación completa de las 32 Vistas CRUD (List, Create, Update, Delete x 8 entidades)
    DepartamentoListView, DepartamentoCreateView, DepartamentoUpdateView, DepartamentoDeleteView,
    EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView,
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView,
    ConsultaMedicaListView, ConsultaMedicaCreateView, ConsultaMedicaUpdateView, ConsultaMedicaDeleteView,
    TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView,
    MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView,
    RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView,
    
    # Importación de los 8 ViewSets API
    DepartamentoViewSet, EspecialidadViewSet, PacienteViewSet, MedicoViewSet, ConsultaMedicaViewSet,
    TratamientoViewSet, MedicamentoViewSet, RecetaMedicaViewSet
)

# Router para las rutas API de Django REST Framework
router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)


urlpatterns = [
     path('', DepartamentoListView.as_view(), name='home'), 
    # -----------------------------------------------------------
    # RUTAS DE LA API
    # -----------------------------------------------------------
    path('api/', include(router.urls)), 

    # -----------------------------------------------------------
    # RUTAS CRUD (TEMPLATES HTML) - 32 rutas definidas
    # -----------------------------------------------------------
    # 1. Departamento
    path('departamentos/', DepartamentoListView.as_view(), name='departamento-list'),
    path('departamentos/crear/', DepartamentoCreateView.as_view(), name='departamento-crear'),
    path('departamentos/<int:pk>/editar/', DepartamentoUpdateView.as_view(), name='departamento-editar'),
    path('departamentos/<int:pk>/eliminar/', DepartamentoDeleteView.as_view(), name='departamento-eliminar'),
    
    # 2. Especialidad
    path('especialidades/', EspecialidadListView.as_view(), name='especialidad-list'),
    path('especialidades/crear/', EspecialidadCreateView.as_view(), name='especialidad-crear'),
    path('especialidades/<int:pk>/editar/', EspecialidadUpdateView.as_view(), name='especialidad-editar'),
    path('especialidades/<int:pk>/eliminar/', EspecialidadDeleteView.as_view(), name='especialidad-eliminar'),
    
    # 3. Paciente
    path('pacientes/', PacienteListView.as_view(), name='paciente-list'),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente-crear'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente-editar'),
    path('pacientes/<int:pk>/eliminar/', PacienteDeleteView.as_view(), name='paciente-eliminar'),
    
    # 4. Medico
    path('medicos/', MedicoListView.as_view(), name='medico-list'),
    path('medicos/crear/', MedicoCreateView.as_view(), name='medico-crear'),
    path('medicos/<int:pk>/editar/', MedicoUpdateView.as_view(), name='medico-editar'),
    path('medicos/<int:pk>/eliminar/', MedicoDeleteView.as_view(), name='medico-eliminar'),
    
    # 5. Consulta_Medica
    path('consultas/', ConsultaMedicaListView.as_view(), name='consultamedica-list'),
    path('consultas/crear/', ConsultaMedicaCreateView.as_view(), name='consultamedica-crear'),
    path('consultas/<int:pk>/editar/', ConsultaMedicaUpdateView.as_view(), name='consultamedica-editar'),
    path('consultas/<int:pk>/eliminar/', ConsultaMedicaDeleteView.as_view(), name='consultamedica-eliminar'),
    
    # 6. Tratamiento
    path('tratamientos/', TratamientoListView.as_view(), name='tratamiento-list'),
    path('tratamientos/crear/', TratamientoCreateView.as_view(), name='tratamiento-crear'),
    path('tratamientos/<int:pk>/editar/', TratamientoUpdateView.as_view(), name='tratamiento-editar'),
    path('tratamientos/<int:pk>/eliminar/', TratamientoDeleteView.as_view(), name='tratamiento-eliminar'),
    
    # 7. Medicamento
    path('medicamentos/', MedicamentoListView.as_view(), name='medicamento-list'),
    path('medicamentos/crear/', MedicamentoCreateView.as_view(), name='medicamento-crear'),
    path('medicamentos/<int:pk>/editar/', MedicamentoUpdateView.as_view(), name='medicamento-editar'),
    path('medicamentos/<int:pk>/eliminar/', MedicamentoDeleteView.as_view(), name='medicamento-eliminar'),
    
    # 8. Receta_Medica
    path('recetas/', RecetaMedicaListView.as_view(), name='recetamedica-list'),
    path('recetas/crear/', RecetaMedicaCreateView.as_view(), name='recetamedica-crear'),
    path('recetas/<int:pk>/editar/', RecetaMedicaUpdateView.as_view(), name='recetamedica-editar'),
    path('recetas/<int:pk>/eliminar/', RecetaMedicaDeleteView.as_view(), name='recetamedica-eliminar'),
]