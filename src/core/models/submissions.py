import uuid

from django.db import models

from src.core.models.problems import Problem


class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    solution = models.TextField()
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)

    class Meta:
        db_table = "submissions"
