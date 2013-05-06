from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Company(models.Model):
    setUp = models.DateField()
    name = models.CharField(max_length=100,unique=True,primary_key=True)
    #image = models.ImageField(upload_to='companies',blank=True)
    
    def __unicode__(self):
        return self.name+'_'+str(self.setUp)

class Platform(models.Model):
    Types=(
        ('PlayStation 3','PlayStation 3'),('Xbox 360','Xbox 360'),('PC','PC'),('Nintendo DS','Nintendo DS'),('Mobile','Mobile'),('PSP','PSP'),
    )
    releaseDate = models.DateField()
    name = models.CharField(max_length=100,choices=Types,unique=True,primary_key=True)
    #image = models.ImageField(upload_to='platforms',blank=True)

    def __unicode__(self):
        return self.name+'_'+str(self.releaseDate)

class Made(models.Model):
    company = models.ForeignKey(Company)
    platform = models.ForeignKey(Platform)
    def __unicode__(self):
        return str(self.company)+'_'+str(self.platform)

class Game(models.Model):
    releaseDate = models.DateField()
    name = models.CharField(max_length=100,unique=True,primary_key=True)
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
        ('Role','Role'),('a','a')
        )
    name = models.CharField(max_length=15,choices=Types,unique=True,primary_key=True)
    def __unicode__(self):
        return self.name

class BelongsTo(models.Model):
    game = models.ForeignKey(Game)
    Type = models.ForeignKey(Type)
    def __unicode__(self):
        return str(self.game)+'_'+str(self.Type)
    
class GameReview(models.Model):
    RATING_CHOICES=((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'))
    rating = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default=3,choices=RATING_CHOICES)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)
    Comment = models.TextField(max_length=255,blank=True)
    game = models.ForeignKey(Game)
