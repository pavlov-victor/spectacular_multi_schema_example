from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class FirstRoute(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'route': 'first'})


class SecondRoute(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'route': 'second'})
