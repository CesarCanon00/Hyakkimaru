from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from bdHakimaru.models import Lugar, Pieza, Monstruo, Pelea, Objeto
from bdHakimaru.forms import pelea_form, monstruo_form, lugar_form, objetos_form

class Home(generic.View):
    model = Pieza
    template_name = 'bdHakimaru/home.html'
    context_object_name = 'obj'        

    def get(self, request):
        piezas = Pelea.objects.filter().count()
        print(piezas)
        context = {'piezas':piezas}
        return render(request, self.template_name,context)

class consultar_demonios(generic.ListView):
    model = Monstruo
    template_name = 'bdHakimaru/monstruo_list.html'
    context_object_name = 'obj'

class consultar_peleas(generic.ListView):
    model = Pelea
    template_name = 'bdHakimaru/consultar_peleas.html'
    context_object_name = 'obj'
    success_url=reverse_lazy("bdHakimaru:Home")

class nueva_pelea(generic.CreateView):
    model = Pelea
    context_object_name = 'obj'
    form_class = pelea_form
    template_name = 'bdHakimaru/nueva_pelea.html'
    success_url=reverse_lazy("bdHakimaru:consultar_peleas")

class nuevo_monstruo(generic.CreateView):
    model = Monstruo
    context_object_name = 'obj'
    form_class = monstruo_form
    template_name = 'bdHakimaru/nuevo_monstruo.html'
    success_url=reverse_lazy("bdHakimaru:consultar_demonios")

class nuevo_lugar(generic.CreateView):
    model = Lugar
    context_object_name = 'obj'
    form_class = lugar_form
    template_name = 'bdHakimaru/nuevo_lugar.html'
    success_url=reverse_lazy("bdHakimaru:Home")

class nuevo_objeto(generic.CreateView):
    model = Objeto
    context_object_name = 'obj'
    form_class = objetos_form
    template_name = 'bdHakimaru/nuevo_objeto.html'
    success_url=reverse_lazy("bdHakimaru:objetos_dororo")

class objeto_list(generic.ListView):
    model = Objeto
    templane_name = 'bdHakimaru/objetos_list.html'
    context_object_name = 'obj'

class borrar_objeto(generic.DeleteView):
    model = Objeto
    template_name = 'bdHakimaru/borrar_objeto.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("bdHakimaru:objetos_dororo")