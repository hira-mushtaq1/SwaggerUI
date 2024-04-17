from .import views
from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    path('user-lists/', UserListAPIView.as_view(), name='user-list'),
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'), 
    path('users/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    path ('login/',LoginAPIView.as_view(), name = 'login'), 
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_question, name='add-question'),
    path('all/', views.view_question, name='view_question'),   
    path('update/<int:pk>/', views.update_question, name='update-question'),
    path('item/<int:pk>/delete/', views.delete_question, name='delete-question'),
    path('save/' , views.save_question, name= "save-question" ),  
]