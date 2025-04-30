from django.urls import path
from .views import QuestionListView

urlpatterns = [
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]
