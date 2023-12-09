import uuid

from django.db import models


class Problem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.TextField()
    testcase_input = models.TextField()
    testcase_output = models.TextField()

    class Meta:
        db_table = "problems"
