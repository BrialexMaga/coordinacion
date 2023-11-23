from django.shortcuts import render
from .forms import StudentCodeForm
from studentform.models import Student
from .models import Course, School_Cycle
from collections import OrderedDict
import pickle
import numpy as np

def searchPage(request):
    if request.method == 'POST':
        form = StudentCodeForm(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            try:
                student = Student.objects.get(code=student_code)
                courses = Course.objects.filter(student=student).order_by('-school_cycle', 'section__subject__key_subject', 'grade_period')

                cycles_list = []
                cycles_index_list = courses.values_list('school_cycle__idCycle', flat=True).distinct()
                for cycleId in cycles_index_list:
                    cycle = School_Cycle.objects.get(idCycle=cycleId)
                    cycles_list.append(cycle)

                cycles_list = list(OrderedDict.fromkeys(cycles_list))

                # Medidas de listas
                #len_list = len(courses)
                #len_cycles = len(cycles_list)

                prediction = predictRisk(student)

                return render(request, 'studenthistory/show_history.html', {'student': student, 'prediction': prediction, 
                                                                            'courses': courses, 'cycles_list': cycles_list#,
                                                                            #'len_list': len_list, 'len_cycles': len_cycles
                                                                            })
            except Student.DoesNotExist:
                form.add_error('student_code', 'No se encontró ningún estudiante con este código.')
    else:
        form = StudentCodeForm()

    return render(request, 'studenthistory/search_page.html', {'form': form})

def predictRisk(student):
    model_path = 'IAmodels/IAmodel.pkl'
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Supongamos que tienes un método para obtener el vector de características del estudiante
    feature_vector = getFeatureVector(student)

    # Realiza la predicción
    #prediction = model.predict(np.array([feature_vector]))

    # Devuelve la predicción (puedes ajustar esto según cómo esté estructurado tu modelo)
    #return prediction[0]
    return 0

def getFeatureVector(student):
    return 0