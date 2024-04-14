from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.tag_name