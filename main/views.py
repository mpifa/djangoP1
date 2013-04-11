# Create your views here.

from django.http import HttpResponse
from  django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.template import Context
from django.template.loader import get_template
from main.models import *
from datetime import datetime
from django.http import Http404
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
        raise Http404
    return render_to_response('info.html',variables)


def xbox360(request):
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
        raise Http404
    return render_to_response('info.html',variables)


def ps3(request):
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
        raise Http404
    return render_to_response('info.html',variables)

def wii(request):
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
        raise Http404
    return render_to_response('info.html',variables)

def vita(request):
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
        raise Http404
    return render_to_response('info.html',variables)

def n3ds(request):
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
        raise Http404
    return render_to_response('info.html',variables)

def mobile(request):
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
    except:
        raise Http404
    return render_to_response('info.html',variables)



def gameDetails(request,ref):   
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.all().filter(game=ref)
    Types = BelongsTo.objects.filter(game=ref)
    Publisher = Game.objects.get(name=ref)
    
    for item in gameInfo:
        elem = [item.game.name]
    types = [str(t.Type.name) for t in Types]
    plat = [str(p.platform.name) for p in gameInfo]
    
    
    variables = Context({
        'titleHead': 'GamesDB',
        'pageTitle': 'Characteristics of '+elem[0],
        'date': Publisher.releaseDate,
        'type':types ,
        'platform':plat,
        'company': Publisher.publisher.name,
        'user': request.user,
    })
    return render_to_response('details.html',variables)

def gameByType(request,ref):
    Types = BelongsTo.objects.filter(Type=ref)
    
    g=[]
    games=({})
    for t in Types:
        g.append(str(t.game.name))
        for ts in g:
            games=SupportedBy.objects.filter(game=ts)
          
    #plat = SupportedBy.objects.filter(name='')
    variables=Context({
        'Title': 'All '+ref+' games',
        'TYPE': games,
        'result': g,
        'user': request.user,

        })
       
    return render_to_response('details2.html',variables)

def gameByCompany(request,ref):
    Company = Game.objects.filter(publisher=ref)
    g=[]
    gl=({})
    llista=[]
    typelist=[]
    llist=[]
    for game in Company:
        g.append(str(game.name))
    for t in g:
        gamelist=SupportedBy.objects.filter(game=t)
        typelist=[]
        for x in gamelist:
            typelist.append(x.platform.name)
        gl.update({x.game.name:typelist})
        llist=[]
        for i in gl.get(t):
            llist.append(i)
        llista.append(llist)
    print llista
    variables=Context({
        'Title': 'All '+ref+' games',
        'TYPE': llista,
        'result': g,
        'user': request.user,

        })
    
    return render_to_response('details3.html',variables)


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

