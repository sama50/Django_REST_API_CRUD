from rest_framework.response import Response
from rest_framework.views import APIView
from .models import userDetails
from .serializers import UserDetailsSeri
from rest_framework import generics



class SnippetList(generics.ListCreateAPIView):
    queryset = userDetails.objects.all()
    serializer_class = UserDetailsSeri

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = userDetails.objects.all()
    serializer_class = UserDetailsSeri
