from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render_to_response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from battle.models import Battle
from .serializers import BattleSerializer
import logging
LOGGER = logging.getLogger(__name__)

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    # renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        try:
            kwargs = eval(request.query_params.get('filters','{}'))
            if not isinstance(kwargs, dict):
                return Response({'error': {"HTTP_400_BAD_REQUEST"},'success':False}, status.HTTP_400_BAD_REQUEST)                
            battle_details = Battle.objects.filter(**kwargs)
            serializer = BattleSerializer(battle_details, many=True)
            return Response({'data':serializer.data,'success':True}, status.HTTP_200_OK)
        except Exception as e:
            print '=================== The exception is "{0}   ================"'.format(e.message)
            return Response({'error': {"HTTP_500_INTERNAL_SERVER_ERROR"},'success':False}, status.HTTP_500_INTERNAL_SERVER_ERROR)