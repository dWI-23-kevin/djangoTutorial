# polls/tests/test_question_api.py

import pytest
from django.urls import reverse
from django.utils import timezone
from polls.tests.factories import QuestionFactory
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_question():
    client = APIClient()
    url = reverse('question-list-create')
    data = {
        "question_text": "Is this a valid question?",
        "pub_date": timezone.now().isoformat()
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["question_text"] == "Is this a valid question?"


@pytest.mark.django_db
def test_get_question():
    question = QuestionFactory()
    client = APIClient()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["question_text"] == question.question_text


@pytest.mark.django_db
def test_update_question():
    question = QuestionFactory()
    client = APIClient()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    data = {
        "question_text": "Updated question text",
        "pub_date": question.pub_date.isoformat()
    }
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["question_text"] == "Updated question text"


@pytest.mark.django_db
def test_delete_question():
    question = QuestionFactory()
    client = APIClient()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
