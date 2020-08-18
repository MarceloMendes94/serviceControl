from django import forms
#from django.forms import Form
from .models import *

class ClientForm(forms.Form):

    class Meta:
        model = Client
        

class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = ('shipName','imoNumber',)

class SeaportForm(forms.ModelForm):
    class Meta:
        model = Seaport
        fields = ('name','country',)

class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ('name',)