from django.db import models
from qux.models import QuxModel


class GizmoModel(QuxModel):
    slug = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=32)
