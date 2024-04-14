from django.db import models
from category.models import Category
from tag.models import Tag

# Create your models here.

class Model3D(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    product_image = models.ImageField(upload_to='model3d/', null=False, blank=False)
    product_description = models.TextField()
    product_fk_category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    product_release_date = models.DateTimeField(auto_now_add=True, )
    product_price = models.FloatField()
    product_height = models.FloatField()
    product_width = models.FloatField()
    product_fk_tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.product_name