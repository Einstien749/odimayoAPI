from rest_framework import serializers

from .models import Africa

class Myserializer(serializers.ModelSerializer):

    class Meta:

        model = Africa

        fields = '__all__'

