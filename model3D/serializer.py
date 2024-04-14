from rest_framework import serializers
from model3D.models import Model3D
from category.serializer import CategorySerializer
from tag.serializer import TagSerializer


class Model3dSerializer(serializers.ModelSerializer):
    # product_fk_category = CategorySerializer()
    # product_fk_tags = TagSerializer(many=True)
    
    class Meta:
        model = Model3D
        fields = '__all__'
        
class model3dSerializerDetail(serializers.ModelSerializer):
    product_fk_category = CategorySerializer()
    product_fk_tags = TagSerializer(many=True)
    
    class Meta:
        model = Model3D
        fields = [
            'product_name', 'product_image', 'product_description',
            'product_fk_category', 'product_release_date', 'product_price',
            'product_height', 'product_width', 'product_fk_tags'
        ]