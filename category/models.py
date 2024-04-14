from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.category_name