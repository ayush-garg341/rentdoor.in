from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class Reviews(APIView):
    def get(self, request, *args, **kwargs):
        response = {"data": [], "message": "Reviews fetched successfully"}

        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        response = {"data": [], "message": "Review added successfully"}

        return Response(response, status=status.HTTP_200_OK)


class ReviewById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = {"data": [], "message": "Review fetched successfully"}

        return response(response, status=status.http_200_ok)

    def put(self, request, *args, **kawrgs):
        response = {"data": [], "message": "review updated successfully"}

        return response(response, status=status.http_200_ok)

    def delete(self, request, *args, **kwargs):
        response = {"data": [], "message": "review deleted successfully"}

        return response(response, status=status.http_200_ok)
