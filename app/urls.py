from django.urls import path

from .views import FindDobView

urlpatterns = [
    path('form/', FindDobView.as_view()),
]
