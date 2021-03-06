from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import *

# Create your models here.

class Company(models.Model):
    setUp = models.DateField(default=date.today)
    name = models.CharField(max_length=100,unique=True,primary_key=True)
    #image = models.ImageField(upload_to='companies',blank=True)
    
    def __unicode__(self):
        return self.name

class Platform(models.Model):
    Types=(
        ('PlayStation 3','PlayStation 3'),('Xbox 360','Xbox 360'),
        ('PC','PC'),('Nintendo DS','Nintendo DS'),('Mobile','Mobile'),('PSP','PSP'),('Wii','Wii')
    )
    releaseDate = models.DateField(default=date.today)
    name = models.CharField(max_length=100,choices=Types,unique=True,primary_key=True)
    #image = models.ImageField(upload_to='platforms',blank=True)

    def __unicode__(self):
        return self.name

class Made(models.Model):
    company = models.ForeignKey(Company)
    platform = models.ForeignKey(Platform)
    def __unicode__(self):
        return str(self.company)+'_'+str(self.platform)

class Game(models.Model):
    releaseDate = models.DateField(default=date.today)
    name = models.CharField(max_length=100,unique=True,primary_key=True)
    publisher = models.ForeignKey(Company)
    def __unicode__(self):
        return self.name

class SupportedBy(models.Model):
    game=models.ForeignKey(Game)
    platform=models.ForeignKey(Platform)
    def __unicode__(self):
        return str(self.game)+'_'+str(self.platform)

class BelongsTo(models.Model):
    game = models.ForeignKey(Game)
    Types=(
        ('Action','Action'),('Adventure','Adventure'),('Simulation','Simulation'),
        ('Sports','Sports'),('Driving','Driving'),('Strategy','Strategy'),('MMO','MMO'),
        ('Role','Role')
        )
    Type = models.CharField(max_length=15,choices=Types)
    def __unicode__(self):
        return str(self.game)+' Type: '+str(self.Type)
    
class GameReview(models.Model):
    RATING_CHOICES=((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'))
    rating = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default=3,choices=RATING_CHOICES)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now)
    Comment = models.TextField(max_length=255,blank=True)
    game = models.ForeignKey(Game)
    platform = models.ForeignKey(Platform)
    city = models.CharField(max_length=100,blank=True)
    def __unicode__(self):
        return str(self.game)+'_'+str(self.user)