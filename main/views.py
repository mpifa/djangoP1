# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from operator import itemgetter
from main.models import *
from datetime import datetime
from main import *
from forms import *
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
def gamesByPlatform(request):
    '''
    This function contains all the games bases on the platform
    '''
    template = get_template('info.html')
    tmp = request.path.split('/')[1]
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
def gameDetails(request,ref):
    '''
    This function show the details of the Game selectes and the platform which
    the belongs to
    '''
    template = get_template('details.html')
    gameInfo = SupportedBy.objects.all().filter(game=ref)
    Types = BelongsTo.objects.filter(game=ref)
    Publisher = Game.objects.get(name=ref)
    Gname = request.path.split('/')[2]
    Reviews = GameReview.objects.all().filter(game=Gname)

    dic=[]
    dic2=({})
    cid=0
    comments = {}
    #try:
    for rv in Reviews:
        cid=cid+1
        dic2=({
                'id': cid,
                'Rid':rv.id,
                'user': str(rv.user),
                'Comment':str(rv.Comment),
                'rate':rv.rating,
                'date':rv.date
                })
        dic.append(dic2)

    for item in gameInfo:
        elem = [item.game.name]
    types = [str(t.Type) for t in Types]
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
        'COMMENTS':'USERS REVIEWS',
        'reviews':dic,
        'path':request.path,
        })
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
    return render_to_response('registration/register.html',{'form':form,'path':request.path},context_instance=RequestContext(request))

@login_required(login_url='/login')
def AddReview(request,pform,ref):
    '''
    Add a review to a game
    '''
    user = request.user
    path = pform+'/'+ref
    path2 = request.path
    if request.method =='POST':
        form = addReviewForm(user,ref,pform,request.POST)
        print form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/'+path)
    else:
        form = addReviewForm(user,ref,pform)
    return render(request,'comment.html',{'form':form,'path':path,'path2':path2,'action':'CREATE'})

def EditReview(request,pform,ref,cid):
    '''
    Function to edit a review
    '''
    user = request.user
    path = pform+'/'+ref
    path2 = request.path
    review = GameReview.objects.get(pk=cid)
    
    Game = str(review.game)
    Rating = str(review.rating)
    Comment = review.Comment
    Platform = str(review.platform)
    
    if review.user != request.user:
        return HttpResponseForbidden()
    if request.method =='POST':
        form = editReviewForm(user,ref,pform,cid,request.POST)
        print request
        if form.is_valid():
            review.delete()
            form.save()
            return HttpResponseRedirect('/'+path)
    else:
        form = editReviewForm(user,ref,pform,cid)
    return render(request,'comment.html',{
                                    'form':form,
                                    'path':path,
                                    'path2':path2,
                                    'action':'EDIT',
                                    'rate':Rating,
                                    'review':Comment,
                                    'game':Game,
                                    'pform':Platform,
                                    'flag':1
                                    })

def DeleteReview(request,pform,ref,id):
    '''
    Function to delete a review
    '''
    rv = GameReview.objects.get(pk=id)
    if rv.user != request.user:
        return HttpResponseForbidden()
    rv.delete()
    return HttpResponseRedirect('/'+pform+'/'+ref)