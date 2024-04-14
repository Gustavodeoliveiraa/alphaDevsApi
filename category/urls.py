from django.urls import path
from category.views import CreateListCategory, RetrieveUpdateDestroyTag
app_name = 'category'

urlpatterns = [
    path('api/v1/category/', CreateListCategory.as_view(), name='list_create'),
    path('api/v1/category/<int:pk>', RetrieveUpdateDestroyTag.as_view(), name='get1_update_delete'),
]
