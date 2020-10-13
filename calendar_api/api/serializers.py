from rest_framework import serializers
from calendar_api.models import *

from rest_framework.generics import *

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'