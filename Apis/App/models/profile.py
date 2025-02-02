from django.db import models
from .base import Base
import uuid

class Profile(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=10, null=True)
    lastname = models.CharField(max_length=10, null=False)
    middlename = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50, unique=True, null=True)
    age = models.PositiveIntegerField(null=True)