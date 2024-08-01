import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from ..models import Question


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = "Sample question?"
    pub_date = factory.LazyFunction(timezone.now)
