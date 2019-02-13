from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.template import loader
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from django.http import (
    HttpResponse,
    HttpResponseRedirect)

from django.shortcuts import render, get_object_or_404, redirect

from .models import StoryPath
from geo_object.models import GeoObject

class PathCreate(CreateView):
    model = StoryPath
    template_name = 'path/path_create.html'
    fields = ['name', 'spots', 'description', 'valid_from','valid_until','source']
    success_url = reverse_lazy("path:list")

class PathList(ListView):
    template_name = 'path/path_list.html'
    context_object_name = 'geoms'

    def get_queryset(self):
        """Return the last five published questions."""
        return StoryPath.objects.order_by('-pub_date')

def delete_path(request, id=None):
    instance = get_object_or_404(StoryPath, id=id)
    instance.delete()
    return redirect("path:list")

class EditPath(UpdateView):
    model = StoryPath
    template_name = 'map.html'
    fields = ['spots', 'name', 'description', 'valid_from','valid_until','source']
    def get_success_url(self, **kwargs):         
        return reverse_lazy("path:info", args=(self.object.id,))


    def get_object(self, queryset=None):
        obj = StoryPath.objects.get(id=self.kwargs['id'])
        return obj


def view_path(request, id=None):
    instance = get_object_or_404(StoryPath, id=id)
    context = {"Path":instance}
    template = loader.get_template('path/view_path.html')
    return HttpResponse(template.render(context,request))

def remove_spot(request, path_id=None, geo_id=None):
    geo_instance = get_object_or_404(GeoObject, id=geo_id)
    path_instance = get_object_or_404(StoryPath, id=path_id)
    path_instance.spots.remove(geo_instance)
    return redirect("path:info", id=path_id )