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
    variables = {
        'titleHead': 'GAMES DATA BASE',
        'pagetitle': 'Welcome to the GamesDB',
        'txt':'',
        'user': request.user,
        }
    return render_to_response('main.html',variables)


def pc(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.filter(platform='PC')   
    variables =Context({
        'Title':"List of PC Games",
        'TYPE':'pc',
        'result': collection,
        'user': request.user,
        
    })
    return render_to_response('info.html',variables)


def xbox360(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Xbox 360')
    variables =Context({
        'Title':"List of Xbox 360 Games",
        'TYPE':'xbox360',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)


def ps3(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='PlayStation 3')
    variables =Context({
        'Title':"List of PlayStation 3 Games",
        'TYPE':'ps3',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)

def wii(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Wii')
    variables =Context({
        'Title':"List of Wii Games",
        'TYPE':'wii',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)

def vita(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Vita')
    variables =Context({
        'Title':"List of Play Station Portable Vita Games",
        'TYPE':'vita',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)

def n3ds(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='N3ds')
    variables =Context({
        'Title':"List of Nintendo 3DS Games",
        'TYPE':'n3ds',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)

def mobile(request):
    template = get_template('info.html')
    collection = SupportedBy.objects.all().filter(platform='Mobile')
    variables =Context({
        'Title':"List of Mobile Games",
        'TYPE':'mobile',
        'result': collection,
        'user': request.user,
    })
    return render_to_response('info.html',variables)


def gameDetails(request,ref):
    #template = get_template('details.html')
    #gameInfo = SupportedBy.objects.get(game=ref)
    #Types = BelongsTo.objects.get(game=ref)
    #Publisher = Game.objects.get(name=ref)
    
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.all().filter(game=ref)
    Types = BelongsTo.objects.all().filter(game=ref)
    Publisher = Game.objects.all().filter(name=ref)
    
    
    variables = Context({
        'titleHead': 'GamesDB',
        'pageTitle': 'Characteristics of '+str(gameInfo),
        'date': Publisher,
        'type':Types ,
        'platform':gameInfo,
        'company': Publisher,
        'user': request.user,
    })
    return render_to_response('details.html',variables)

def userpage(request,username):
    try:
        user=User.objects.get(username=username)
    except:
        raise Http404('User not foun.')
    template = get_template('log.html')
    variables = Context({
        'username': username,
    })
    output = template.render(variables)
    return HttpResponse(output)

