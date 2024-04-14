from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from model3D.models import Model3D
from model3D.serializer import Model3dSerializer, model3dSerializerDetail


class ListCreate3DModel(generics.ListCreateAPIView):
    queryset = Model3D.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return model3dSerializerDetail
        return Model3dSerializer


class RetrieveUpdateDestroy3dModel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model3D.objects.all()
    serializer_class = Model3dSerializer

class Retrieve3dModelByName(APIView):

    def get(self, *args, **kwargs):
        query_string_name = kwargs.get('name')
        
        if query_string_name:
            queryset = Model3D.objects.filter(product_name__icontains=query_string_name)
            serializer = Model3dSerializer(queryset, many=True)
            return  Response(serializer.data, status=status.HTTP_200_OK)
        