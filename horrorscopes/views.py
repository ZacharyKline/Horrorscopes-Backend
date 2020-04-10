from rest_framework import viewsets
from horrorscopes import models, serializers



class ZodiacViewSet(viewsets.ModelViewSet):
    queryset = models.Zodiac.objects.all()
    serializer_class = serializers.ZodiacSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagsSerializer

class HoroscopesViewSet(viewsets.ModelViewSet):
    queryset = models.Horoscope.objects.all()
    serializer_class = serializers.HoroscopeSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = models.Element.objects.all()
    serializer_class = serializers.ElementSerializer