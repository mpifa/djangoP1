from django.forms import ModelForm
from main.models import *

class addReviewForm(ModelForm):
    def __init__(self,user,pform,Game,*args,**kwrds):
        super(addReviewForm,self).__init__(*args,**kwrds)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        #self.fields['game'].queryset = Game.objects.filter(game)
        #self.fields['platform'].queryset = 
    class Meta:
        model=GameReview
class editReviewForm(ModelForm):
    class Meta:
        model=GameReview