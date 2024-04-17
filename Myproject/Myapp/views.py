# from rest_framework.response import Response
# from rest_framework import permissions
# from rest_framework import  generics,status
# from .serializers import LoginSerializer,UserSerializers
# from .models import User
# from .permission import IsLoggedInUserOrAdmin, IsAdminUser
# from rest_framework.permissions import IsAuthenticated

# #for viewing all user with admin permission
# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsAuthenticated,IsAdminUser]
# # to signup by anyone
# class UserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [permissions.AllowAny]
# #view user detail by authenticated user or admin
# class UserRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsLoggedInUserOrAdmin]
# # update user profile by authenticate user
# class UserUpdateAPIView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsAuthenticated,IsLoggedInUserOrAdmin]


# #delete user by only admin
# class UserDestroyAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsAuthenticated,IsAdminUser]
# #login users
# class LoginAPIView(generics.GenericAPIView):
#     serializer_class=LoginSerializer
#     permission_classes=[permissions.AllowAny]
#     def post(self, request):
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception= True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics, status
from .serializers import LoginSerializer, UserSerializers
from .models import User
from .permission import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
 

from rest_framework import status

from Myproject.Myapp import serializers

# For viewing all users with admin permission
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

# To signup by anyone
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]

# View user detail by authenticated user or admin
class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsLoggedInUserOrAdmin]

# Update user profile by authenticated user
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

# Delete user by only admin
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

# Login users
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




# Create your views here.
# basic apis view
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete',
        'save': '/save'
    }
 
    return Response(api_urls)

 


@api_view(['POST'])  # add questions api
def add_question(request):
    item = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:

        return Response(status=status.HTTP_404_NOT_FOUND)

    
@api_view(['GET'])
def view_question(request): # view questions api
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])  # update questions api
def update_question(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE']) # delete question api
def delete_question(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST']) # save question api
def save_question(request):
    item = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:

        return Response(status=status.HTTP_404_NOT_FOUND)  