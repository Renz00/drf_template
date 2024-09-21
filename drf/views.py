from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True) # many=True since drinks is a list containing rows
    # serializer = DrinkSerializer(drinks, fields=['id', 'name'], many=True) # specify the model fields to return
    return Response({ "drinks": serializer.data, "msg": "success" }, status=status.HTTP_200_OK)


@api_view(['POST'])
def store(request):
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "drink": serializer.data, "msg": "success" }, status=status.HTTP_201_CREATED)
    
    return Response({ "msg": "invalid" }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show(request, id: int):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response({ "msg": "failed" }, status=status.HTTP_404_NOT_FOUND)
        
    serializer = DrinkSerializer(drink)
    return Response({ "drink": serializer.data, "msg": "success" }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, id: int):
    try:
        drink = Drink.objects.get(pk=id) # pk = primary key
    except Drink.DoesNotExist:
        return Response({ "msg": "failed" }, status=status.HTTP_404_NOT_FOUND)
        
    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "drink": serializer.data, "msg": "success" }, status=status.HTTP_200_OK)
    
    return Response({ "msg": "invalid" }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id: int):
    try:
        Drink.objects.get(pk=id).delete()
        return Response({ "msg": "success" }, status=status.HTTP_200_OK)
    
    except Drink.DoesNotExist:
        return Response({ "msg": "failed" }, status=status.HTTP_404_NOT_FOUND)