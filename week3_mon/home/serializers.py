from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class peopleserilazers(serializers.ModelSerializer):
    
    class Meta:
        model = person
        fields = '__all__'
        
        
class blogserilazers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'     
        
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True) 
    
    class Meta:
        model = User    
        fields = ['username','email','password']  
        
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )  
        
        return user          
    
    
    
class LoginSerialize(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)  
    
    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        
        if not user:
                raise serializers.ValidationError("Invalid username or password")

        data['user'] = user  
        return data