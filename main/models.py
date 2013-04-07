from django.db import models

# Create your models here.

class Company(models.Model):
    setUp = models.DateTimeField()
    name = models.TextField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name

class Platform(models.Model):
    releaseDate = models.DateTimeField()
    name = models.TextField(max_length=100,unique=True)
    company = models.ForeignKey(Company)
    #company = models.TextField(max_length=100)
    def __unicode__(self):
        return self.name

class Type(models.Model):
    Types=(
        ('Action','Act'),('Adventure','Adv'),('Simulation','Sim'),
        ('Sports','Spt'),('Driving','Drv'),('Strategy','Str'),('MMO','MMO'),
        ('Role','Role')
        )
    name = models.CharField(max_length=15,choices=Types,unique=True)
    def __unicode__(self):
        return self.name

class Joc(models.Model):
    releaseDate = models.DateTimeField()
    name = models.TextField(max_length=100,unique=True)
    platform= models.ManyToManyField(Platform)
    company = models.ForeignKey(Company)
    types = models.ManyToManyField(Type)
    def __unicode__(self):
        return self.name+" | "+self.company.name+" | "+self.gender