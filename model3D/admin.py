from django.contrib import admin
from model3D.models import Model3D

# Register your models here.
@admin.register(Model3D)
class Model3dAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'product_image', 'product_description',
        'product_fk_category', 'product_release_date', 'product_price', 
        'product_height', 'product_width', 
    )