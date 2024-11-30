from django import forms

class EstudianteForm(forms.Form):
    rango_edad = forms.CharField(label='Rango de edad', max_length=50, required=False)
    gen_alu = forms.ChoiceField(
        label='Género',
        choices=[(1, 'Masculino'), (2, 'Femenino')],
        required=False
    )


class SQLQueryForm(forms.Form):
    QUERY_CHOICES = [('universidad', 'Universidad'),]
    QUERY_CHOICES2 = [('carrera','Carrera')]
    QUERY_CHOICES3 = [('edad','Edad')]
    QUERY_CHOICES4 = [('sexo','Sexo')]
                       
    query_type = forms.ChoiceField(choices=QUERY_CHOICES, label='Tipo de Consulta por Universidad')
    parameter = forms.CharField(max_length=100, required=False, label='Parámetro de Búsqueda: Universidad')

    query_type2 = forms.ChoiceField(choices=QUERY_CHOICES2, label='Tipo de Consulta por Carrera')
    parameter2 = forms.CharField(max_length=100, required=False, label='Parámetro de Búsqueda: Carrera')

    query_type3 = forms.ChoiceField(choices=QUERY_CHOICES3, label='Tipo de Consulta por Edad')
    parameter3 = forms.CharField(max_length=100, required=False, label='Parámetro de Búsqueda: Edad')

    query_type4 = forms.ChoiceField(choices=QUERY_CHOICES4, label='Tipo de Consulta por Género')
    parameter4 = forms.CharField(max_length=100, required=False, label='Parámetro de Búsqueda: Masculino (insertar 1), Femenino (insertar 2)')

    















