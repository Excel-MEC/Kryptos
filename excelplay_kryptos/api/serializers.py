from rest_framework import serializers
from .models import Level, KryptosUser
from django.forms.fields import FileField


class LevelSerializer(serializers.ModelSerializer):
    file = FileField()

    class Meta:
        fields = (
            'id',
            'level',
            'answer',
            'source_hint',
        )
        model = Level


class KryptosUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'user_id',
            'level',
            'rank',
        )
        model = KryptosUser
