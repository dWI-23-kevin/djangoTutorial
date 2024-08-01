from django.utils import timezone
from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def validate(self, data):
        if data['pub_date'] > timezone.now():
            raise serializers.ValidationError("The publication date cannot be in the future.")
        return data

    def validate_question_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("The question must be at least 10 characters long.")
        return value
