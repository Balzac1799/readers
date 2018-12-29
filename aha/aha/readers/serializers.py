from aha.readers.models import Reader 
from rest_framework import serializers


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('id', 'phone')