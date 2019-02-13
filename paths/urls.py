
from django.urls import path, reverse
from .views import PathCreate, PathList, delete_path, EditPath, view_path, remove_spot


app_name = 'path'
urlpatterns = [
    path('new/', PathCreate.as_view(), name='create'),
    path('list/',  PathList.as_view(), name='list'),
    path('<int:id>/delete/', delete_path, name='delete'),
    path('<int:id>/edit/', EditPath.as_view() , name='edit'),
    path('<int:id>/', view_path, name='info'), 
    path('<int:path_id>/remove/<int:geo_id>', remove_spot, name='remove_spot'),   
]
