from django.urls import path
from tag.views import ListCrateTags, RetrieveUpdateDeleteTag

app_name = 'tag'
urlpatterns = [
    path('api/v1/tags/', ListCrateTags.as_view(), name='list_create_tag'),
    path('api/v1/tags/<int:pk>', RetrieveUpdateDeleteTag.as_view(), name='retrieve_update_delete_tag')
]
