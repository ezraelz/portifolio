from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')

        # Create Profile
        profile = User.objects.create(
            **validated_data
        )
        profile.set_password(password)
        profile.save()

        return profile
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): 
    username_field = 'username' 
    
    def validate(self, attrs): 
        data = super().validate(attrs) 
        return data

