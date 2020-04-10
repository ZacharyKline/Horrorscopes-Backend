from rest_framework.serializers import HyperlinkedModelSerializer
from horrorscopes.models import Zodiac, Tags, Horoscope, Element

class ZodiacSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Zodiac
        fields = [
            'zodiac_name',
            'subtitle',
            'insight',
            'friendship',
            'love',
            'strengths',
            'weakness',
            'likes',
            'dislikes',
            'shade_of_insanity',
            'date-range'
        ]

class HoroscopeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Horoscope
        fields = [
            'post_date',
            'zodiac',
            'horror',
            'id'
        ]


class TagsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = [
            'tag',
            'id'
        ]

class ElementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = [
            'id',
            'element_type',
            'description'
        ]