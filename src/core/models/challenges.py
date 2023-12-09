import uuid

from django.db import models

from src.core.models.problems import Problem


class Challenge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    problems = models.ManyToManyField(Problem)

    class Meta:
        db_table = "challenges"
