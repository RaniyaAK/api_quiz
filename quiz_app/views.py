from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Quiz
from . serializers import QuizSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status


@api_view (['GET'])
def quiz(request):
    quizzes= Quiz.objects.all()
    serializer= QuizSerializer(quizzes,many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view (['POST'])
def add_quiz(request):
    is_many = isinstance(request.data,list)
    serializer= QuizSerializer(data= request.data,many= is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_quiz(request,quiz_id):
    student= get_object_or_404(Quiz,id=quiz_id)
    serializer= QuizSerializer(student,data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_quiz(request,quiz_id):
    quiz = get_object_or_404(Quiz,id=quiz_id)
    quiz.delete()
    return Response({'message':f"The Quiz with ID {quiz_id} is deleted successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view (['GET'])
def search_quiz(request):
    query=request.GET.get('q','')
    quizzes=Quiz.objects.filter(
        Q(question__icontains=query) |
        Q(option_a__icontains=query) |
        Q(option_b__icontains=query) |
        Q(option_c__icontains=query) |
        Q(option_d__icontains=query)
        )

    serializer= QuizSerializer(quizzes,many= True)
    return Response(serializer.data,status=status.HTTP_200_OK)

