from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import Universidad, Carrera, Estudiante
from django.db import connection
from django import forms
from collections import namedtuple
from django.shortcuts import render, redirect
from .forms import EstudianteForm
from .forms import SQLQueryForm

# Create your views here.     

def namedtuplefetchall(cursor):
    "Devuelve todas las filas de un cursor como namedtuples"
    desc = cursor.description
    nt_result = namedtuple('Resultado', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def menu_consultas(request):
    resultados = None
    error = None

    if request.method == 'POST':
        form = SQLQueryForm(request.POST)
        if form.is_valid():
            query_type = form.cleaned_data['query_type']
            parameter = form.cleaned_data['parameter']

            query_type2 = form.cleaned_data['query_type2']
            parameter2 = form.cleaned_data['parameter2']

            query_type3 = form.cleaned_data['query_type3']
            parameter3 = form.cleaned_data['parameter3']

            query_type4 = form.cleaned_data['query_type4']
            parameter4 = form.cleaned_data['parameter4']

            try:
                with connection.cursor() as cursor:
                    # Iniciamos la consulta SQL
                    sql_query = """
                        SELECT cat_periodo,anio_ing_carr_ori, gen_alu, rango_edad, nomb_inst,
                               nomb_carrera, dur_total_carr, nivel_global
                        FROM titulados
                        WHERE 1=1
                    """
                    params = []

                    # Agregamos condiciones según los parámetros proporcionados
                    if query_type == 'universidad' and parameter:
                        sql_query += " AND nomb_inst LIKE %s"
                        params.append(f"%{parameter}%")

                    if query_type2 == 'carrera' and parameter2:
                        sql_query += " AND nomb_carrera LIKE %s"
                        params.append(f"%{parameter2}%")

                    if query_type3 == 'edad' and parameter3:
                        sql_query += " AND rango_edad = %s"
                        params.append(parameter3)
                    
                    if query_type4 == 'sexo' and parameter4:
                        sql_query += " AND gen_alu = %s"
                        params.append(parameter4)

                    # Ejecutamos la consulta con todas las condiciones aplicadas
                    cursor.execute(sql_query, params)
                    resultados = namedtuplefetchall(cursor)
            except Exception as e:
                error = f"Error al realizar la consulta: {e}"
        else:
            error = "Formulario inválido. Por favor, revise los campos ingresados."
    else:
        form = SQLQueryForm()

    return render(request, 'menu_consultas.html', {'form': form, 'resultados': resultados, 'error': error})









