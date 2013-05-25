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
        
class addGameForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(addGameForm,self).__init__(*args,**kwrds)
        self.fields['releaseDate'].help_text = "* (dd/mm/yyyy)"
    class Meta:
        model=Game
class addCompanyForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(addCompanyForm,self).__init__(*args,**kwrds)
        self.fields['setUp'].help_text = "* (dd/mm/yyyy)"
    class Meta:
        model=Company
        
class addGameToPlatForm(ModelForm):
    def __init__(self,gm,*args,**kwrds):
        super(addGameToPlatForm ,self).__init__(*args,**kwrds)
        self.fields['game'].empty_label = None
        self.fields['game'].queryset = Game.objects.all().filter(name=gm)
    class Meta:
        model=SupportedBy
        
class asgnGameTypeOfGameForm(ModelForm):
    def __init__(self,gm,*args,**kwrds):
        super(asgnGameTypeOfGameForm,self).__init__(*args,**kwrds)
        self.fields['game'].empty_label = None
        self.fields['game'].queryset = Game.objects.all().filter(name=gm)
    class Meta:
        model=BelongsTo

#        
#class editGameForm(ModelForm):
#    def __init__(self,user,*args,**kwrds):
#        super(editGameForm,self).__init__(*args,**kwrds)
#                
#        #self.fields['user'].empty_label= None
#        #self.fields['user'].queryset = User.objects.filter(username=user)
#        #
#        #self.fields['game'].empty_label= None
#        #self.fields['game'].queryset = Game.objects.filter(name=gm)
#        #
#        #self.fields['platform'].empty_label= None
#        #self.fields['platform'].queryset = Platform.objects.filter(name=pform)
#        #
#    class Meta:
#        model=Game