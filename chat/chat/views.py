from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import TokenSerializer
from .services import chatbot


class CreateMessageView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serialiezer = self.get_serializer(data=request.data)
        serialiezer.is_valid(raise_exception=True)
        message = chatbot(serialiezer.validated_data["token"])
        print(message)
        return Response(data={"token": message}, status=200)
