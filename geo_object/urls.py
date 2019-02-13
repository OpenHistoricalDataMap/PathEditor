from django.urls import path, reverse

from .views import (
    CreateGeoObj,
    EditGeoObj,
    delete_geo_obj,
    view_geo_obj,
    ListGeoObj,
    geo_obj_index
)


app_name = 'geo_object'
urlpatterns = [
    # List all geo_objects
    path('', geo_obj_index, name='index'),
    # create new geo_object
    path('new/', CreateGeoObj.as_view(), name='create'),
    # List all geo_objects
    path('list/', ListGeoObj.as_view(), name='list'),
    # delete object based on id
    path('delete/<int:id>/', delete_geo_obj, name='delete'),
    # view object based on id
    path('<int:id>/', view_geo_obj, name='info'),
    # edit object based on id
    path('<int:id>/edit', EditGeoObj.as_view(), name='edit'),
   
]
