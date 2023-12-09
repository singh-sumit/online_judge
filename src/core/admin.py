from django.contrib import admin

from src.core.models import Challenge, Problem, Submission

# Register your models here.
admin.site.register([
    Challenge,
    Problem,
    Submission
])
