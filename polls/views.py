from django.shortcuts import render
from .models import Question

def question_list(request):
    # отримуємо всі об’єкти Question
    questions = Question.objects.all()
    context = {'questions': questions}
    # вказуємо шлях до шаблону polls/question_list.html
    return render(request, 'polls/question_list.html', context)
