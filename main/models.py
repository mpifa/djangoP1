from django.db import models

# Create your models here.

class Company(models.Model):
    setUp = models.DateField()
    name = models.TextField(max_length=100,unique=True,primary_key=True)
    def __unicode__(self):
        return self.name+'_'+str(self.setUp)

class Platform(models.Model):
    releaseDate = models.DateField()
    name = models.TextField(max_length=100,unique=True,primary_key=True)
    def __unicode__(self):
        return self.name+'_'+str(self.releaseDate)

class Made(models.Model):
    company = models.ForeignKey(Company)
    platform = models.ForeignKey(Platform)
    def __unicode__(self):
        return str(self.company)+'_'+str(self.platform)

class Game(models.Model):
    releaseDate = models.DateField()
    name = models.TextField(max_length=100,unique=True,primary_key=True)
    publisher = models.ForeignKey(Company)
    def __unicode__(self):
        return self.name+'_'+str(self.publisher)+'_'+str(self.releaseDate)

class SupportedBy(models.Model):
    game=models.ForeignKey(Game)
    platform=models.ForeignKey(Platform)
    def __unicode__(self):
        return str(self.game)+'_'+str(self.platform)
    
class Type(models.Model):
    Types=(
        ('Action','Action'),('Adventure','Adventure'),('Simulation','Simulation'),
        ('Sports','Sports'),('Driving','Driving'),('Strategy','Strategy'),('MMO','MMO'),
        ('Role','Role')
        )
    name = models.CharField(max_length=15,choices=Types,unique=True,primary_key=True)
    def __unicode__(self):
        return self.name

class BelongsTo(models.Model):
    game = models.ForeignKey(Game)
    Type = models.ForeignKey(Type)
    def __unicode__(self):
        return str(self.game)+'_'+str(self.Type)
