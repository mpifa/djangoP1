# Create your views here.

from django.http import HttpResponse
from  django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.template import Context
from django.template.loader import get_template
from main.models import *
from main import *


def mainpage(request):
    template = get_template('tmp.html')
    variables = Context({
        'titleHead': 'GAMES DATA BASE',
        'pagetitle': 'Welcome to a GamesDB',
        'contentbody': "",
        'user': request.user,
        })
    output = template.render(variables)
    return HttpResponse(output)

def pc(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'TYPE':'pc',
        'result': SupportedBy.objects.all().filter(platform='PC'),
        'Url': SupportedBy.objects.all().filter(platform='PC')
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def xbox360(reques):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'xbox360',
        'result': SupportedBy.objects.all().filter(platform='Xbox 360'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def ps3(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'ps3',
        'result': SupportedBy.objects.all().filter(platform='PlayStation 3'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def wii(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'wii',
        'result': SupportedBy.objects.all().filter(platform='Wii'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def vita(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'vita',
        'result': SupportedBy.objects.all().filter(platform='PSP Vita'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def n3ds(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'n3ds',
        'result': SupportedBy.objects.all().filter(platform='Nintendo 3DS'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def mobile(request):
    template = get_template('mainpage.html')
    variables =Context({
        'Title':"List of PC Games",
        'Type':'mobile',
        'result': SupportedBy.objects.all().filter(platform='Mobile'),
        
    })
    output = template.render(variables)
    return HttpResponse(output)

def gameDetails(request):
    template = get_template('details.html')
    variables = Context({
        'titleHead': 'GamesDB',
        'pagetTitle': '',
        'name':'',
        'date':'',
        'type': '',
        'platform':'',
        'company':''
    })
    output = template.render(variables)
    return HttpResponse(output)

def logout(request):
    logout(request)
    param = { 'titlehead' : "Log out",
            'state': ""}
    return render_to_response('mainpage.html',param)

def userpage(request,username):
    try:
        user=User.objects.get(username=username)
    except:
        raise Http404('User not foun.')
    jocs = user.jocs_set.all()
    template = get_template('userpage.html')
    variables = Context({
        'username': username,
        'jocs': jocs
        })
    output = template.render(variables)
    return HttpResponse(output)
