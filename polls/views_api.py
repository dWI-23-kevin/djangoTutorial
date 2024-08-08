from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Question
from .serializers import QuestionSerializer


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]