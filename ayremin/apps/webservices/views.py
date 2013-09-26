from ayremin.apps.moduloAcademico.models import Matricula, Estudiante
from django.http import HttpResponse
from django.core import serializers

def wsMatriculas_view(request):
	try:
		estudiante = Estudiante.objects.get(usuario = request.user)
	except:
		estudiante = None
	data = serializers.serialize("json", Matricula.objects.filter(estudiante = estudiante))
	return HttpResponse(data, mimetype='application/json')	

