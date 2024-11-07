from django.urls import path
from .views import TasksView


urlpatterns = [
    path('api/task/', TasksView.as_view(), name="tasks"),
]