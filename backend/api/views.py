from django.shortcuts import render
from rest_framework import generics, viewsets

from rest_framework.response import Response
from rest_framework.views import APIView



from .serializers import NewsSerializer
# from . import serializers

from apps.bulb.models import News, Comments



class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class GetCapitalInfoView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы Capital
        queryset = News.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = NewsSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)