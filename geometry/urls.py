from django.urls import path, reverse
from .views import GeoCreate, geo_info, GeoList, geo_delete, EditGeometry, geo_index


app_name = 'geometry'
urlpatterns = [
    # Create new Geometry
    path('new/', GeoCreate.as_view(), name='create'),
    # List all Geometries
    path('list/', GeoList.as_view(), name='list'),
    # Delete Geometry based on ID
    path('<int:id>/delete', geo_delete, name='delete'),
    # Edit Geometry based on ID
    path('<int:id>/edit', EditGeometry.as_view(), name='edit'),
    # Inspect Geometry based on ID
    path('<int:id>/', geo_info, name='info'),    
    # Index listing all Geometries
    path('', geo_index, name='index'),    
]
