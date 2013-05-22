# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from main.models import *
from datetime import datetime
from main import *

from forms import ReviewForm
from django import forms


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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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


@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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



@login_required(login_url='/login')
def gameDetails(request,ref):
    '''
    This function show the details of the Game selectes and the platform which
    the belongs to
    '''
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.all().filter(game=ref)
    Types = BelongsTo.objects.filter(game=ref)
    Publisher = Game.objects.get(name=ref)
    #Reviews = GameReview.objects.all().filter(game=ref)
    Gname = request.path.split('/')[2]
    Reviews = GameReview.objects.all().filter(game=Gname)
    print Reviews
    dic=({})
    dic2=({})
    cid=0
    comments = {}    
    #try:
    for rv in Reviews:
        cid=cid+1
        dic2=({
                'id': cid,
                'user': str(rv.user),
                'Comment':str(rv.Comment),
                'rate':rv.rating,
                })
                
        dic[str(cid)]=dic2
    print dic
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
        'COMMENTS':'COMMENTS',
        'reviews':dic,
        'path':request.path,
        })
    #except:
        #variables = Context({
        #    'titleHead': 'GamesDB',
        #    'user': request.user,
        #    'Message':'This requested Game does not exist!',
        #})
        #return render_to_response('http404.html',variables)
    return render_to_response('details.html',variables)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def Logout(request):
    '''
    This function logout the use and redirects him
    '''
    logout(request)
    return redirect('/')
def register(request):
    '''
    '''
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form= UserCreationForm()
    return render_to_response('registration.html',{'form':form},context_instance=RequestContext(request))
#def Comment(request,mode):
#    '''
#    Load comment template
#    '''
#    variables=Context({
#        'user':request.user,
#        'mode':mode,
#    })
#    return render_to_response('comment.html',variables)

@login_required(login_url='/login')
def AddComment(request,pform,ref):
    '''
    '''
    user = request.user
    path = request.path.split('/')
    path = path[3]+'/'+path[4]
    path2 = request.path
    
    print path2
    if request.method =='POST':
        form = addReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/'+path)
    else:
        form = addReviewForm()
    return render(request,'comment.html',{'form':form,'path':path,'path2':path2})

def EditComment(request,pform,ref):
    user = request.user
    path = request.path.split('/')
    path = path[3]+'/'+path[4]
    path2 = request.path
    
    print path2
    if request.method =='POST':
        form = editReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/'+path)
    else:
        form = editReviewForm()
    return render(request,'comment.html',{'form':form,'path':path,'path2':path2})

def DeleteComment(request,pform,ref):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ReviewForm()
    return render(request,'comment.html',{'form':form})