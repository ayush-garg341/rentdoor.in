from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheck(APIView):
    def get(self, request, *args, **kwargs):
        response = {"data": [], "message": "Django is up and running"}

        return Response(response, status=status.HTTP_200_OK)
