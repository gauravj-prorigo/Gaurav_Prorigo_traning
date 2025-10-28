from rest_framework import serializers
from .models import *

class peopleserilazers(serializers.ModelSerializer):
    
    class Meta:
        model = person
        fields = '__all__'
        
        
class blogserilazers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'      