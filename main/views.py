# Create your views here.

from django.http import HttpResponse
from  django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.template import Context
from django.template.loader import get_template
from main.models import *
from datetime import datetime
from django.http import Http404
from main import *




def mainpage(request):
    '''
    This function contains the main template as initial website
    '''
    template = get_template('main.html')
    variables = {
        'titleHead': 'GAMES DATA BASE',
        'pagetitle': 'Welcome to the GamesDB',
        'user': request.user,
        }
    return render_to_response('main.html',variables)


def pc(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='PC'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'user': request.user,
            'Message':'Games not added yet! ',
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)


def xbox360(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='Xbox 360'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'user': request.user,
            'Message':'Games not added yet! ',
        })
        return render_to_response('http404.html',variables)

    return render_to_response('info.html',variables)


def ps3(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='PlayStation 3'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'user': request.user,
            'Message':'Games not added yet! ',
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)

def wii(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='Wii'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'user': request.user,
            'Message':'Games not added yet! ',
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)

def vita(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='PSP'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'Message':'Games not added yet! ',
            'user': request.user,
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)

def n3ds(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='Nintendo DS'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'Message':'Games not added yet! ',
            'user': request.user,
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)

def mobile(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp='Mobile'
    try:
        coll = Made.objects.get(platform=tmp)
        collection = SupportedBy.objects.all().filter(platform=tmp)
            
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'TYPE':tmp,
            'Date': coll.platform.releaseDate,
            'Made':coll.company.name,
            'set':coll.company.setUp,
            'result': collection,
            'user': request.user,
        })
        def action():
            return render_to_response('comments.html')
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'Message':'Games not added yet! ',
            'user': request.user,
        })
        return render_to_response('http404.html',variables)
    return render_to_response('info.html',variables)



def gameDetails(request,pform,ref):
    '''
    This function show the details of the Game selectes and the platform which
    the belongs to
    '''
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.all().filter(game=ref,platform=pform)
    Types = BelongsTo.objects.filter(game=ref)
    Publisher = Game.objects.get(name=ref)
    try:    
        for item in gameInfo:
            elem = [item.game.name]
        types = [str(t.Type.name) for t in Types]
        plat = [str(p.platform.name) for p in gameInfo]
        variables = Context({
            'titleHead': 'GamesDB',
            'pageTitle': 'Characteristics of '+elem[0],
            'name':elem[0],
            'date': Publisher.releaseDate,
            'type':types ,
            'platform':plat,
            'company': Publisher.publisher.name,
            'user': request.user,
        })
    except:
        variables = Context({
            'titleHead': 'GamesDB',
            'user': request.user,
            'Message':'This requested Game does not exist!',
        })
        return render_to_response('http404.html',variables)
    return render_to_response('details.html',variables)

def gameByType(request,ref):
    '''
    This function shows all the games by type
    '''
    try:
        Types = BelongsTo.objects.filter(Type=ref)   
        g=[]
        for t in Types:
            g.append(str(t.game.name))
        variables=Context({
            'Title': 'All '+ref+' games',
            'result': g,
            'user': request.user,
    
            })
    except:
        raise Http404   
    return render_to_response('details3.html',variables)

def gameByCompany(request,ref):
    '''
    This function shows all the games by company
    '''
    try:    
        Company = Game.objects.filter(publisher=ref)
        g=[]
        for game in Company:
            g.append(str(game.name))
        variables=Context({
            'Title': 'All '+ref+' games',
            'result': g,
            'user': request.user,
    
            })
    except:
        raise Http404
    return render_to_response('details3.html',variables)

def Logout(request):
    '''
    This function logout the use and redirects him
    '''
    logout(request)
    return redirect('/')
