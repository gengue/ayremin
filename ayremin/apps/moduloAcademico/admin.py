from ayremin.apps.moduloAcademico.models import Facultad, Programa, Materia, Semestre, Estudiante, Matricula
from django.contrib import admin

admin.site.register(Facultad)
admin.site.register(Programa)
admin.site.register(Materia)
admin.site.register(Semestre)
admin.site.register(Estudiante)
admin.site.register(Matricula)