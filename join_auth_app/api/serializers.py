from rest_framework import serializers
from django.contrib.auth.models import User
from join_auth_app.models import JoinUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only = True)
    name = serializers.EmailField(source="user.username", read_only = True)
    class Meta:
        model = JoinUser
        exclude = ["user", "id"]


class FindUserByToken(serializers.Serializer):
    token = serializers.CharField(write_only=True)
    def validate(self, data):
        token = data.get("token")
        token = Token.objects.filter(key=token).first()
        user = token.user
        print(user)
        if (token):
            return {
                "isToken": True,
                "name": user.username,  
                "email": user.email
            }
        return {"isToken": False}


class IsEmailAlreadyInDataBaseSerilializer(serializers.Serializer):
    email =serializers.CharField(write_only=True)
    def validate(self, data):
        data["isValidEmail"] = True
        email = data.get("email")
        user_exists = User.objects.filter(email=email).exists()
        return {
            "email": email,
            "isValidEmail": not user_exists,
        }
        

class LoginSerializer(serializers.Serializer):  
    username = serializers.CharField(write_only=True)  
    password = serializers.CharField(write_only=True)  

    def validate(self, data):
        email_or_password = data.get("username")
        password = data.get("password")
        user = None
        if "@" in email_or_password:
            try:
                user = User.objects.get(email = email_or_password)
            except User.DoesNotExist:
                raise serializers.ValidationError("Wrong Email")
        else:
            try:
                user = User.objects.get(username = email_or_password)
            except User.DoesNotExist:
                raise serializers.ValidationError("Wrong Name")

        if not user or not user.check_password(password):
            raise serializers.ValidationError("Wrong Password.")

        data["user"] = user
        return data



class RegistrationSerializer(serializers.ModelSerializer):  
    password = serializers.CharField(write_only=True) 
    email = serializers.EmailField(write_only=True) 
    repeated_password = serializers.CharField(default="", write_only=True)
    username = serializers.CharField(write_only=True) 
    userID = serializers.CharField(default="")

    def save(self):
        pw = self.validated_data["password"]
        email = self.validated_data["email"]
        userID = self.validated_data["userID"]
        username = self.validated_data["username"]
        if not userID:
            raise serializers.ValidationError("No UserID in Body as Request")
        if pw != self.validated_data["repeated_password"]:
            raise serializers.ValidationError("Passwords doesn't match!")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email is already registered!"})
        user = User.objects.create_user(username=username, email=email, password=pw)
        join_user = JoinUser.objects.create(user=user, userID=userID)
        join_user.save()
        return join_user 
    
    class Meta:
        model = JoinUser
        fields = ["userID", "password", "repeated_password", "email", "username"]


        