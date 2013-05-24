from django.forms import ModelForm
from main.models import *

class addReviewForm(ModelForm):
    def __init__(self,user,gm,pform,*args,**kwrds):
        super(addReviewForm,self).__init__(*args,**kwrds)
        self.fields['user'].empty_label= None
        self.fields['user'].queryset = User.objects.filter(username=user)
        
        self.fields['game'].empty_label= None
        self.fields['game'].queryset = Game.objects.filter(name=gm)
       
        self.fields['platform'].empty_label= None
        self.fields['platform'].queryset = Platform.objects.filter(name=pform)
        
    class Meta:
        model=GameReview
        exclude=('date',)
        
class editReviewForm(ModelForm):
    def __init__(self,user,gm,pform,*args,**kwrds):
        super(editReviewForm,self).__init__(*args,**kwrds)
                
        self.fields['user'].empty_label= None
        self.fields['user'].queryset = User.objects.filter(username=user)
        
        self.fields['game'].empty_label= None
        self.fields['game'].queryset = Game.objects.filter(name=gm)
        
        self.fields['platform'].empty_label= None
        self.fields['platform'].queryset = Platform.objects.filter(name=pform)
        
    class Meta:
        model=GameReview        
        exclude=('date')