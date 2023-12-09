from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.api.v1.auth.views.login import LoginViewSet
from src.api.v1.problems.views import ProblemModelViewSet

app_name = "api.v1"

# router
router = DefaultRouter()

router.register(r'problems', ProblemModelViewSet, basename="problems")

urlpatterns = [
    path('', include(router.urls)),

    path('auth/login', LoginViewSet.as_view(), name="user-login"),
]
