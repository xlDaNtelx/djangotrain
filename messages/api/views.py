from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from messages.models import Message
from .serializers import (
    MessageSerializer,
    MessageCreateSerializer,
    MessageSingleSerializer,
)


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageSingleAPIView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSingleSerializer


class MessageUpdateAPIView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSingleSerializer


class MessageDestroyAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSingleSerializer

# class MessageCreateAPIView(CreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
