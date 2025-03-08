
from rest_framework.views import APIView 
from rest_framework import generics, status
from join_auth_app.models import JoinUser
from .serializers import RegistrationSerializer, UserSerializer, LoginSerializer, IsEmailAlreadyInDataBaseSerilializer, FindUserByToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken


class AllJoinUsersView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer =  UserSerializer(JoinUser.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class JoinUserView(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer =  UserSerializer(JoinUser.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer =  UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            JoinUser.objects.all().delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        serializer = UserSerializer(JoinUser.objects.get(pk=pk))
        JoinUser.objects.get(pk=pk).delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            saved_user = serializer.save()
            token, create = Token.objects.get_or_create(user= saved_user.user)
            data = {
                "message":'Account succesfully created',
                "username":  saved_user.user.username,
                "email":  saved_user.user.email,
                "token": token.key
                    }
        else:
            data = serializer.errors
        return Response(data,  status=status.HTTP_201_CREATED)
    
class LoginView(ObtainAuthToken):
     permission_classes = [AllowAny]
     def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            auth_user = serializer.validated_data["user"]
            token, create = Token.objects.get_or_create(user=auth_user)
            data = {
                "message":'Login was succesfully',
                "username": auth_user.username,
                "email": auth_user.email,
                "token": token.key
                    }
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_202_ACCEPTED)

class ValidationOfEmailView(APIView):
     permission_classes = [AllowAny]
     def post(self, request):
        serializer = IsEmailAlreadyInDataBaseSerilializer(data = request.data)
        if serializer.is_valid():
            data = {"isValidEmail" : serializer.validated_data["isValidEmail"]}
            return Response(data = data, status=status.HTTP_202_ACCEPTED)
        return Response (data = serializer.data, status=status.HTTP_400_BAD_REQUEST)
     
class FindUserByTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = FindUserByToken(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(data = data, status=status.HTTP_202_ACCEPTED)
        return Response (data = serializer.data, status=status.HTTP_400_BAD_REQUEST)