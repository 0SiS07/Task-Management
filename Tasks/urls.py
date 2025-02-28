from django.urls import path
from Tasks.views import Show_Task

urlpatterns = [
    path('Show_Task/',Show_Task)
]
