from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET'])
def home(request):
    stu_obj = Student.objects.all()
    serializer = StudentSerializer(stu_obj,many=True)

    return Response({'status': 200, 'payload': serializer.data})
