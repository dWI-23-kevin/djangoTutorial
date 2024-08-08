import pytest
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

from polls.tests.factories import QuestionFactory


@pytest.fixture
def api_client():
    user = User.objects.create_user(username='admin', password='1234')
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.mark.django_db
def test_create_question(api_client):
    url = reverse('question-list-create')
    data = {
        "question_text": "Is this a valid question?",
        "pub_date": timezone.now().isoformat()
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["question_text"] == "Is this a valid question?"

@pytest.mark.django_db
def test_get_question(api_client):
    question = QuestionFactory()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["question_text"] == question.question_text

@pytest.mark.django_db
def test_update_question(api_client):
    question = QuestionFactory()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    data = {
        "question_text": "Updated question text",
        "pub_date": question.pub_date.isoformat()
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["question_text"] == "Updated question text"

@pytest.mark.django_db
def test_delete_question(api_client):
    question = QuestionFactory()
    url = reverse('question-retrieve-update-destroy', args=[question.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
