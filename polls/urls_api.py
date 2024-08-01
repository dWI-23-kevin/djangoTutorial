from django.urls import path

from .views_api import QuestionListCreate, QuestionRetrieveUpdateDestroy

urlpatterns = [
    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroy.as_view(), name='question-retrieve-update-destroy'),
]
