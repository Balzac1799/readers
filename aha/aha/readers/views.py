from rest_framework import viewsets
from aha.readers.models import Reader 
from aha.readers.serializers import ReaderSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer