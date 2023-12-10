from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.api.v1.auth.views.login import LoginViewSet
from src.api.v1.challenges.views import ChallengeModelViewSet
from src.api.v1.problems.views import ProblemModelViewSet
from src.api.v1.submissions.views import SubmissionModelViewSet

app_name = "api.v1"

# router
router = DefaultRouter()

router.register(r'problems', ProblemModelViewSet, basename="problems")
router.register(r'submissions', SubmissionModelViewSet, basename="submissions")
router.register(r'challenges', ChallengeModelViewSet, basename="challenges")

urlpatterns = [
    path('', include(router.urls)),

    path('auth/login', LoginViewSet.as_view(), name="user-login"),
]
