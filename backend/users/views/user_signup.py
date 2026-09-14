from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSignup

class UserSignupView(APIView):
    def post(self,request,format=None):
        data=request.data
        serializer=UserSignup(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'User signup successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)