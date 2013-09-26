from django.shortcuts import render_to_response
from django.template import RequestContext
from ayremin.apps.moduloAcademico.models import Matricula, Materia, Estudiante
from ayremin.apps.moduloAcademico.forms import ContactForm, loginForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponseRedirect
from datetime import datetime

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/miInfo')
    else:
        if request.method == "POST":
            form = loginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/miInfo')
                else:
                    mensaje = "usuario y/o password incorrecto"
        form = loginForm()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response('moduloAcademico/login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def info_view(request):
    try:
        estudiante = Estudiante.objects.get(usuario = request.user)
    except:
        estudiante = None
    nombre = estudiante.usuario.get_full_name()
    periodoIngreso = estudiante.periodoIngreso
    programa = estudiante.programa.nombre
    facultad = estudiante.programa.Facultad.nombre
    ctx = {'estudiante':nombre, 'ingreso':periodoIngreso,'programa':programa, 'facultad':facultad}
    return render_to_response('moduloAcademico/miInformacion.html', ctx, context_instance=RequestContext(request))

def hojadevida_view(request):
    try:
        estudiante = Estudiante.objects.get(usuario = request.user)
    except:
        estudiante = None
    materia = Matricula.objects.filter(estudiante = estudiante) 
    ctx = {'materias':materia}
    return render_to_response('moduloAcademico/hojadevida.html', ctx, context_instance=RequestContext(request))

def contacto_view(request):
    info_enviado = False #Definir si se envio la informacion o no se envio
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']
            # Configuracion enviado mensaje via gmail
            to_admin = 'genesisdaft@gmail.com'
            html_content = "Informacion Recibida de [%s]<br><br>**Mensaje**<br>%s"%(email, texto)
            msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    else:   

        formulario = ContactForm()  
    ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto, 'info_enviado':info_enviado}
    return render_to_response('moduloAcademico/contacto.html', ctx,context_instance=RequestContext(request))