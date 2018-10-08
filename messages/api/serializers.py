from rest_framework.serializers import ModelSerializer
from messages.models import Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'title',
            'description',
            'count',
        ]


class MessageSingleSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'title',
            'description',
            'count',
        ]


class MessageCreateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'title',
            'description',
            'count',
        ]
