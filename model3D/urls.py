from model3D.views import (
    ListCreate3DModel, RetrieveUpdateDestroy3dModel, Retrieve3dModelByName
)
from django.urls import path

app_name = '3d_model'

urlpatterns = [
    path('api/v1/model/3d_model', ListCreate3DModel.as_view(), name='list'),
    path('api/v1/model/3d_model/<int:pk>/', RetrieveUpdateDestroy3dModel.as_view(), name='create'),
    path('api/v1/model/search_3d_model/<str:name>', Retrieve3dModelByName.as_view(), name='get_by_name'), 
]
