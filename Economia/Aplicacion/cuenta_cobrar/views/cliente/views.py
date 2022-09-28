from django.urls import reverse_lazy
from django.views.generic import *
from Aplicacion.cuenta_cobrar.models import Cliente
from Aplicacion.cuenta_cobrar.forms import *


# MENÚ
class MenuCobro(TemplateView):
    template_name = 'menu_seleccion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['listar_url'] = '/menu'
        return context


# TABLA
class DetalleCliente(ListView):
    template_name = 'cliente/detalle_clientes.html'
    context_object_name = 'cliente'
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/cuenta_cobrar/tarjetas/'
        context['listar_url'] = '/cuenta_cobrar/tarjetas/'
        context['titulo'] = 'Registro de clientes'

        return context


# REGISTRO
class CrearCliente(CreateView):
    model = Cliente
    template_name = 'cliente/crearcliente.html'
    form_class = Clientes
    success_url = reverse_lazy("cuenta_cobrar:detalle_cliente")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de clientes'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/cuenta_cobrar/tarjetas/'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente/'

        return context


class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'
    success_url = reverse_lazy('cuenta_cobrar:detalle_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Clientes'
        context['url_anterior'] = '/cuenta_cobrar/detalle_cliente'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente'

        return context

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = "cliente/editar_cliente.html"
    success_url = reverse_lazy('cuenta_cobrar:detalle_cliente')
    form_class = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Actualizar Datos de Cliente'
        context['url_anterior'] = '/cuenta_cobrar/detalle_cliente'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente'

        return context