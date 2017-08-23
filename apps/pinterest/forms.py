from django.forms import ModelForm
from .models import Pin, Board

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'description', 'image', 'topic']

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description']