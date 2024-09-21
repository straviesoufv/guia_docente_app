from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('upload/', views.upload_view, name='upload'),
    path('reformular_descripcion/', views.reformulate_description, name='reformular_descripcion'),
    path('expand_contenido/', views.expand_content, name='expandir_contenido'),
    path('expandir_actividades/', views.expand_activities_content, name='expandir_actividades'),
    path('expandir_resultados_aprendizaje/', views.expand_resultados_aprendizaje_content, name='expandir_resultados_aprendizaje'),
    path('expandir_sistema_evaluacion_aprendizaje/', views.expand_sistema_evaluacion_aprendizaje_content, name='expandir_sistema_evaluacion_aprendizaje'),
    path('crear_actividades_ftp/', views.formar_para_transformar, name='crear_actividades_ftp'),
    path('calendarizar_actividades/', views.calendarizacion, name='calendarizar_actividades'),
    path('pagina_intermedia_rubrica/', views.rubrica_pagina_intermedia, name='pagina_intermedia_rubrica'),
    path('generar_rubrica_evaluacion/', views.generar_rubrica_evaluacion, name='generar_rubrica_evaluacion'),
    path('descargar_rubrica_xlsx/', views.descargar_rubrica_xlsx, name='descargar_rubrica_xlsx'),
    path('subir_apuntes/', views.upload_apuntes_view, name='subir_apuntes'),
    path('dashboard_apuntes/', views.dashboard_apuntes_view, name='dashboard_apuntes'),
    path('puntos_clave_apuntes/', views.puntos_clave_view, name='puntos_clave_apuntes'),
    path('faqs_apuntes/', views.faqs_view, name='faqs_apuntes'),
    path('glosario_apuntes/', views.glosario_view, name='glosario_apuntes'),
    path('caso_practico_apuntes/', views.caso_practico_view, name='caso_practico_apuntes'),
    path('preguntas_tipo_test_apuntes/', views.tipo_test_view, name='preguntas_tipo_test_apuntes'),
    path('descargar_qti_tipo_test_apuntes/', views.descargar_qti_view, name='descargar_qti_tipo_test_apuntes'),
    path('extraer_temas/', views.extraer_temas_apuntes, name='extraer_temas_apuntes'),
    path('pagina_intermedia_actividades/', views.actividades_pagina_intermedia_apuntes, name='pagina_intermedia_actividades'),
    path('actividades_evaluacion_resultado/', views.generar_actividades_evaluacion, name='actividades_evaluacion_resultado'),
    path('descargar_descripcion/', views.download_reformulated_description, name='descargar_descripcion'),


    # Añade más rutas según las funcionalidades
]
