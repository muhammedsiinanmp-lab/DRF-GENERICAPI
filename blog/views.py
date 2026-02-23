from django.shortcuts import render
from rest_framework import generics,mixins
from .serializers import PostSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response

# class LoginView(APIView):
#     permission_classes =[ AllowAny]
#     def post(self,request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username,password=password)

#         if user:
#             login(request,user)
#             return Response({"Message":"Login Successfull"})
#         return Response({"Errors":"Invalid Credentials"})
    
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         logout(request)
#         return Response({"Message":"Logged Out"})


class UserList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class PostList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
    

class PostDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def get(self,request,slug):
        return self.retrieve(request)
    
    def put(self,request,slug):
        return self.update(request)
    
    def delete(self,request,slug):
        return self.destroy(request)