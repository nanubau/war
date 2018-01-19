from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging
LOGGER = logging.getLogger(__name__)

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from battle.models import Battle
from .serializers import BattleSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

# factory = APIRequestFactory()
# request = factory.get('/')
# serializer_context = {
#     'request': Request(request),
# }

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        kwargs = eval(request.query_params.get('filters'))
        user_count = Battle.objects.filter(**kwargs)
        # print user_count
        # content = {'user_count': user_count}
        serializer = BattleSerializer(user_count, many=True)
        # return Response(serializer)    
        # print user_count.to_json()
        print serializer
        json = JSONRenderer().render(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
        print '\n\n\n\n'
        print json
        print '\n\n\n\n'
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data, status.HTTP_200_OK)
