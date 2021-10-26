from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import QuestionForm, Answer
from django import forms
class QuestionModelForm(ModelForm):
    class Meta:
        model = QuestionForm
        fields = ['name', 'ques']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['ans']