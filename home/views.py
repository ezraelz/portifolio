from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Faq, CollectEmails
from .serializers import FaqSerializer,CollectEmailsSerializer


@api_view(['POST'])
def submit_contact(request):
    serializer = FaqSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Thank you for your message!'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_data(request):
    datas = Faq.objects.all()
    serializer = FaqSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def collect_email(request):
    serializer = CollectEmailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Thank you I will contact you soon.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    