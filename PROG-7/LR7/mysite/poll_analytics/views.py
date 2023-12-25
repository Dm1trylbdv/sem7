from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

def index(request):
    questions = Question.objects.order_by('pub_date')
    context = {"context_list" : []}

    for q in questions:
        choices = Choice.objects.filter(question_id=q.pk)
        labels, values = [], []
        for row in choices:
            labels.append(row.choice_text)
            values.append(row.votes)
        context_item = {
            "title": q.question_text,
            "labels": labels,
            "values": values
        }
        context['context_list'].append(context_item)

    return render(request, "poll_analytics/index.html", context)


@api_view(['GET'])
def question_collection(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def question_element(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    

@api_view(['GET'])
def choice_collection(request):
    if request.method == 'GET':
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def choices_for_question(request, q):
    try:
        choices = Choice.objects.filter(question_id=q)
    except choices.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)