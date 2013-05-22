from django.forms import ModelForm
from main.models import *

class addReviewForm(ModelForm):
    class Meta:
        model=GameReview
class editReviewForm(ModelForm):
    class Meta:
        model=Gamereview