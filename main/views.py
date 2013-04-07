# Create your views here.

from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template
from main.models import Game
from main.models import *
from main import *


def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Games DB',
        'pagetitle': 'Welcome to a GamesDB',
        'contentbody': models.Made.objects.all()
        })
    output = template.render(variables)
    return HttpResponse(output)

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