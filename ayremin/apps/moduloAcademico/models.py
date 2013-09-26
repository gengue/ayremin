#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Facultad(models.Model):
	nombre = models.CharField(max_length=150)
	def __unicode__(self):
		return self.nombre

class Programa(models.Model):
	nombre = models.CharField(max_length=150)
	Facultad = models.ForeignKey(Facultad)
	codigoPublico = models.PositiveIntegerField(null=False)

	def __unicode__(self):
		return self.nombre

class Materia(models.Model):
	nombre = models.CharField(max_length=250, null=False)
	programa = models.ForeignKey(Programa)
	creditos = models.PositiveIntegerField()

	def __unicode__(self):
		return self.nombre

class Semestre(models.Model):
	periodo = models.CharField(max_length=5)
	def __unicode__(self):
		return self.periodo

class Estudiante(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    programa = models.ForeignKey(Programa)
    periodoIngreso = models.ForeignKey(Semestre)

    def __unicode__(self):
    	return unicode(self.usuario)

class Matricula(models.Model):
	estudiante = models.ForeignKey(Estudiante)
	materia = models.ForeignKey(Materia)
	nota = models.PositiveIntegerField()
	semestre = models.ForeignKey(Semestre)

	def __unicode__(self):
		return "%s - %s"%(unicode(self.estudiante), self.materia)
