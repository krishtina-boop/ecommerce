from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from users.serializers import UserLoginSerializer
from users.serializers import JWTSerializer

class UserLoginView(APIView):
    def post(Self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.validated_data.get('email')
            password=serializer.validated_data.get('password')
            user=authenticate(email=email, password=password)

            if user is not None:
                refresh = JWTSerializer.get_token(user)
                return Response({
                    'access':str(refresh.access_token),
                    'refresh':str(refresh),
                    'email':user.email,
                    'role':user.role,
                    'message': 'login successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error':{'email or password invalid'}}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
