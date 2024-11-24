from rest_framework import serializers
from .models import Faq,CollectEmails

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
        
class CollectEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectEmails
        fields = '__all__'