# Create your views here.

from django.http import HttpResponse
from  django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.template import Context
from django.template.loader import get_template
from main.models import *
from datetime import datetime
from main import *


def mainpage(request):
    template = get_template('main.html')
    variables = Context({
        'titleHead': 'GAMES DATA BASE',
        'pagetitle': 'Welcome to a GamesDB',
        'contentbody': "",
        'user': request.user,
        })
    output = template.render(variables)
    return HttpResponse(output)

def pc(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='PC')
    variables =Context({
        'Title':"List of PC Games",
        'TYPE':'pc',
        'NAME': '',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def xbox360(reques):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Xbox 360')
    variables =Context({
        'Title':"List of Xbox 360 Games",
        'TYPE':'xbox360',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def ps3(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='PlayStation 3')
    variables =Context({
        'Title':"List of PlayStation 3 Games",
        'TYPE':'ps3',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def wii(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Wii')
    variables =Context({
        'Title':"List of Wii Games",
        'TYPE':'wii',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def vita(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Vita')
    variables =Context({
        'Title':"List of Play Station Portable Vita Games",
        'TYPE':'vita',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def n3ds(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='N3ds')
    variables =Context({
        'Title':"List of Nintendo 3DS Games",
        'TYPE':'n3ds',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def mobile(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Mobile')
    variables =Context({
        'Title':"List of Mobile Games",
        'TYPE':'mobile',
        'NAME':'',
        'result': collection,        
    })
    output = template.render(variables)
    return HttpResponse(output)

def gameDetails(request,ref):
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.get(game=ref)
    Types = BelongsTo.objects.get(game=ref)
    Publisher = Game.objects.get(name=ref)
    
    variables = Context({
        'titleHead': 'GamesDB',
        'pageTitle': 'Characteristics of '+str(gameInfo.game),
        'date': Publisher.releaseDate,
        'type':Types.Type ,
        'platform':gameInfo.platform,
        'company': Publisher.publisher,
    })
    output = template.render(variables)
    return HttpResponse(output)
    
def logout(request):
    logout(request)
    param = { 'titlehead' : "Log out",
            'state': ""}
    return render_to_response('main.html',param)

