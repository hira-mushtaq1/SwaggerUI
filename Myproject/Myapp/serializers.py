from rest_framework import  serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import Item

#-----------User model--------------------#

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

#-------------------login serializer-----------------------------------#


# login serializer start here
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68, min_length=6,write_only=True)
    username=serializers.CharField(max_length=255,min_length=3, read_only=True)
    tokens=serializers.SerializerMethodField()
    def get_tokens(self,obj):
        user = User.objects.get(email=obj['email'])        
        return {
    'access':user.tokens()['access'],
    'refresh':user.tokens()['refresh']
            } 
    class Meta:
        model=User
        fields=['email','password','username','tokens']     
        def validate(self, attrs):
            email = attrs.get('email', '')
            password=attrs.get('password', '')         
            user = auth.authenticate(email=email, password=password)         
            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')        
            attrs['user'] = user
            return attrs
        
#-----------------Item=questions model------------------#
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('Question', 'Created','Created_By', 'Title', 'Department' )