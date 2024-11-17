from django.shortcuts import render
from .models import Question

def quiz_view(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        correct = 0
        wrong = 0

        for question in questions:
            # Get the selected options for each question as a list of IDs
            selected_option_ids = request.POST.getlist(f'question_{question.id}')
            selected_options = question.options.filter(id__in=selected_option_ids)

            # Get all correct options for the question
            correct_options = question.options.filter(is_correct=True)

            # Check if the selected options match the correct ones
            if set(selected_options) == set(correct_options):
                correct += 1
            else:
                wrong += 1

        return render(request, 'quiz/result.html', {'correct': correct, 'wrong': wrong})

    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})
