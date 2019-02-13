from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.template import loader
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from .models import GeoObject

from django.http import (
    HttpResponse,
    HttpResponseRedirect)

from django.shortcuts import render, get_object_or_404, redirect

# Inspect a Geometry Object based on ID
def view_geo_obj(request, id=None):
    instance = get_object_or_404(GeoObject, id=id)
    context = {"GeoObj":instance}
    template = loader.get_template('obj/view_geom.html')
    return HttpResponse(template.render(context,request))

# Create a new Geometry Object
class CreateGeoObj(CreateView):
    model = GeoObject
    template_name = 'obj/map.html'
    fields = ['geom', 'geom_id', 'name', 'description', 'valid_from','valid_until','source']
    success_url = reverse_lazy("geo_object:list")


# List all Geometry Object
class ListGeoObj(ListView):
    template_name = 'obj/geom_list.html'
    context_object_name = 'geoms'
    def get_queryset(self):
        #<WSGIRequest: GET '/obj/list/'>
        """Return the last five published questions."""
        return GeoObject.objects.order_by('-id')

# Delete Geometry Object based on ID
def delete_geo_obj(request, id=None):
    instance = get_object_or_404(GeoObject, id=id)
    #<WSGIRequest: GET '/obj/delete/4/'>
    instance.delete()
    return redirect("geo_object:list")

# Edit Geometry Object based on ID
class EditGeoObj(UpdateView):
    model = GeoObject
    template_name = 'map.html'
    fields = ['geom', 'geom_id', 'name', 'description', 'valid_from','valid_until','source']
    success_url = reverse_lazy("geo_object:list")

    def get_object(self, queryset=None):
        obj = GeoObject.objects.get(id=self.kwargs['id'])
        return obj

# Index Site listing Objects
def geo_obj_index(request):  
    template = loader.get_template('obj/geo_obj_index.html')
    context = {}
    return HttpResponse(template.render(context,request))