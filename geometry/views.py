from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.template import loader
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from django.http import (
    HttpResponse,
    HttpResponseRedirect)

from django.shortcuts import render, get_object_or_404, redirect

from .models import Geometry

# Create new Geometry
class GeoCreate(CreateView):
    model = Geometry
    template_name = 'geometry/map.html'
    fields = ['geom', 'geom_id']
    success_url = reverse_lazy("geometry:list")

# Inspect Geometry based on ID
def geo_info(request, id=None):
    instance = get_object_or_404(Geometry, id=id)
    context = {"Geometry":instance}
    template = loader.get_template('geometry/geo_detail.html')
    return HttpResponse(template.render(context,request))
# List all Geometries
class GeoList(ListView):
    template_name = 'geometry/geo_list.html'
    context_object_name = 'geoms'

    def get_queryset(self):
        """Return the last five published questions."""
        return Geometry.objects.order_by('-pub_date')

# Edit Geometry based on ID
class EditGeometry(UpdateView):
    model = Geometry
    template_name = 'map.html'
    fields = ['geom']
    def get_success_url(self, **kwargs):         
        return reverse_lazy("geometry:info", args=(self.object.id,))


    def get_object(self, queryset=None):
        obj = Geometry.objects.get(id=self.kwargs['id'])
        return obj
# Delete Geometry based on ID
def geo_delete(request, id=None):
    instance = get_object_or_404(Geometry, id=id)
    instance.delete()
    return redirect("geometry:list")

# INdex listing all Geometries
def geo_index(request):  
    template = loader.get_template('geometry/geo_index.html')
    context = {}
    return HttpResponse(template.render(context,request))
