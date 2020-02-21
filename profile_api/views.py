from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers


class HelloApiView(APIView):
    """dtest Api View."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiView = [
            'User HTTP methods as funtion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'gives you the most control over you app logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """hanle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """handle delete an object"""
        return Response({'method': 'DELETE'})
