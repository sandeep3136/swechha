from django.db import models
from ckeditor.fields import RichTextField

class QuestionForm(models.Model):
    name = models.CharField(max_length=100)
    ques = models.TextField()
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "  " + self.ques

class Answer(models.Model):
    ques = models.ForeignKey(QuestionForm, on_delete=models.CASCADE)
    ans = RichTextField(blank=True, null=True)
 