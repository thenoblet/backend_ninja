from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import basic_info
from .serializers import basic_info_serializer
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
def get_basic_info(request):
        info = basic_info.objects.first()
        #print(f"Data before serialization: {basic_info.__dict__}")
        serializer = basic_info_serializer(info)
        return Response(serializer.data)
        