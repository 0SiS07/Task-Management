from django.urls import path
from Tasks.views import Show_Task,Show_Specific_Task

urlpatterns = [
    path('Show_Task/',Show_Task),
    path('Show_Task/<int:id>/',Show_Specific_Task)
]
