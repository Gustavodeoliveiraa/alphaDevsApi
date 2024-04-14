from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from tag.models import Tag
from tag.serializer import TagSerializer


class ListCrateTags(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RetrieveUpdateDeleteTag(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer