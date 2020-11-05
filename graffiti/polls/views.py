from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import QuestionSerializer, ChoiceSerializer

from .models import Question

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse( response % question_id)

# def vote(request,question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# IDK what this line means
# @csrf_exempt
def question_list(request):
    # List questions, JSON
    if request.method == 'GET':
        questions = Question.objects.all()
        # Serialize all as JS object
        serializer = QuestionSerializer(questions, many=True)
        # Return JSON
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def question_detail(request, pk):
    # Get single question
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)