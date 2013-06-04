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
from datetime import *
from main import *
from forms import *
from django import forms

def mainpage(request):
    '''
    This function contains the main template as initial website
    '''
    template = get_template('main.html')
    variables = {
        'titleHead': 'GAMES DATABASE',
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
    path = request.path
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
            'path': path,
        })
    except:
        variables =Context({
            'Title':'List of '+tmp+' Games',
            'user': request.user,
            'Message':'Games not added yet! ',
            'path':path,
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
                'Comment':rv.Comment,
                'rate':rv.rating,
                'date':rv.date,
                'city':str(rv.city),
                })
        dic.append(dic2)
    dic = sorted(dic, key=lambda k: k['date'])
    
    for item in gameInfo:
        elem = [item.game.name]
    types = [str(t.Type) for t in Types]
    plat = [str(p.platform.name) for p in gameInfo]
    variables = Context({
        'titleHead': 'GamesDB',
        'pageTitle': 'Characteristics of ',
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
    #except:
    #    variables = Context({
    #         'titleHead': 'GamesDB',
    #         'user': request.user,
    #         'Message':'This requested Game does not exist!',
    #    })
    #    return render_to_response('http404.html',variables)
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
    return render(request,'comment.html',{'form':form,'path':path,'path2':path2,'action':'CREATE REVIEW','flag':3})

@login_required(login_url='/login')
def EditReview(request,pform,ref,cid):
    '''
    Function to edit a review
    '''
    user = request.user
    path = pform+'/'+ref
    path2 = request.path
    review = GameReview.objects.get(pk=cid)
    
    Rid = review.id
    Game = str(review.game)
    Rating = str(review.rating)
    Comment = review.Comment
    Platform = str(review.platform)
    
    if review.user != request.user:
        return HttpResponseForbidden()
    if request.method =='POST':
        form = editReviewForm(user,ref,pform,request.POST,instance = review)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/'+path)
    else:
        form = editReviewForm(user,ref,pform, instance = review)
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
@login_required
def DeleteReview(request,pform,ref,id):
    '''
    Function to delete a review
    '''
    rv = GameReview.objects.get(pk=id)
    if rv.user != request.user:
        return HttpResponseForbidden()
    rv.delete()
    return HttpResponseRedirect('/'+pform+'/'+ref)

@login_required(login_url='/login')
def addGame(request):
    '''
    Add a game using a form
    '''
    user = request.user
    current = request.path
    if request.method =='POST':
        form = addGameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/asgnTypeOfGame/'+form.cleaned_data['name'])
    else:
        form = addGameForm()
    return render(request,'comment.html',{'form':form,'path':"/addCompany/",'path2':current,'action':'CREATE GAME','flag':2,'tag':'Add publisher'})

def deleteGame(request,pform,gm):
    '''
    Delete a game requested using its platform and game
    '''
    sup = SupportedBy.objects.all().filter(game = gm,platform=pform)
    rev = GameReview.objects.all().filter(game = gm,platform=pform)
    
    sup.delete()
    rev.delete()
    
    if not (SupportedBy.objects.all().filter(game = gm)):
        bel = BelongsTo.objects.all().filter(game = gm)
        gm = Game.objects.get(name = gm)
        
        bel.delete()
        gm.delete()

    return HttpResponseRedirect('/'+pform)

def addCompany(request):
    '''
    Add company
    '''
    user = request.user
    current = request.path
    if request.method =='POST':
        form = addCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addGame')
    else:
        form = addCompanyForm()
    return render(request,'comment.html',{'form':form,'path':"/addGame",'path2':current,'action':'CREATE GAME','flag':4,'tag':'Back'})

def addGameToPlat(request,game):
    '''
    Assign game to platform
    '''
    user = request.user,
    current = request.path
    if request.method =='POST':
        form = addGameToPlatForm(game,request.POST)
        if form.is_valid():
            try:
                if SupportedBy.objects.get(game=form.cleaned_data['game'],  platform= form.cleaned_data['platform']):
                    return HttpResponseRedirect(current)
            except: 
                form.save()
                return HttpResponseRedirect('/addGameToPlat/'+game)        
    else:
        form = addGameToPlatForm(game)
    return render(request,'comment.html',{'form':form,'path':"/",'game':game,'path2':current,'action':'CREATE GAME','flag':2,'method':'REPOST','tag':'Finish'})

def asgnTypeOfGame(request,game):
    '''
    Assign game to its type
    '''
    ser = request.user
    current = request.path
    if request.method =='POST':
        form = asgnGameTypeOfGameForm(game,request.POST)

        if form.is_valid():
            try:
                if BelongsTo.objects.get(game=form.cleaned_data['game'],  Type= form.cleaned_data['Type']):
                    return HttpResponseRedirect(current)
            except: 
                form.save()
                return HttpResponseRedirect('/asgnTypeOfGame/'+game)
    else:
        form = asgnGameTypeOfGameForm(game)
    return render(request,'comment.html',{'form':form,'game':game,'path':"/addGameToPlat/"+game,'path2':current,'action':'CREATE GAME','flag':2,'method':'REPOST','tag':'Next'})
