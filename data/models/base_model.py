from django.db import models

class BaseModel(models.Model):
    """Base model for all other models."""
    class Meta:
        abstract = True
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
