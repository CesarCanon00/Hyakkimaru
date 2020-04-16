from django import forms
from bdHakimaru.models import Monstruo, Pelea, Pieza, Lugar, Objeto

class pelea_form(forms.ModelForm):
    class Meta:
        model = Pelea
        fields = ['lugar','monstruo']
        labels = {'lugar': 'Lugar' , 'monstruo':'Monstruo'}
        #widget = {'lugar': forms.TextInput(),'monstruo':forms.TextInput()}
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class monstruo_form(forms.ModelForm):
    class Meta:
        model = Monstruo
        fields = ['nombre','imagen','pieza','lugar']
        labels = {'nombre':'Nombre','imagen':'Imagen','pieza':'Pieza','lugar':'Lugar'}
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class lugar_form(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre','imagen']
        labels = {'nombre':'Nombre', 'imagen':'Imagen'}
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class objetos_form(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre','origen']
        labels = {'nombre':'Nombre', 'origen':'Origen'}
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

