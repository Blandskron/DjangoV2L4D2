from django.shortcuts import render, get_object_or_404
from .models import Question

def trivia_game(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'trivia/trivia_game.html', context)

def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option_id = request.POST.get('option')
        
        try:
            question = Question.objects.get(pk=question_id)
            correct_option = question.option_set.get(is_correct=True)
            
            if selected_option_id == str(correct_option.id):
                message = "¡Correcto!"
            else:
                message = f"Incorrecto. La respuesta correcta era: {correct_option.text}"
        except Question.DoesNotExist:
            message = "La pregunta no existe."
        except correct_option.DoesNotExist:
            message = "La opción correcta para esta pregunta no existe."
        
        return render(request, 'trivia/answer.html', {'message': message})
