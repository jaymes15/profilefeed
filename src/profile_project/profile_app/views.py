from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import models
from . import permissions
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    #Testing APIView

    serializer_class = serializers.HelloSerializer



    def get(self,request,format= None):
        #GET request

        apiview = ['hello','hey','how you doing']
        message = {'message':apiview}
        return Response(message)

    def post(self,request):
        #post request name field

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)
            success_message = {'message':message}
            return Response(success_message)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        apiview = 'put method'
        message = {'message':apiview}
        return Response(message)

    def patch(self,request,pk=None):
        #only uodates fields provided in the request
        apiview = 'patch method'
        message = {'message':apiview}
        return Response(message)

    def delete(self,request,pk=None):
        #delete
        apiview = 'delete method'
        message = {'message':apiview}
        return Response(message)



class HelloViewSet(viewsets.ViewSet):

    def list(self,request):
        #get all objects
        apiview = ['viewset','hey','how you doing']
        message = {'message':apiview}
        return Response(message)

    def create(self,request):
        #post request name field

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)
            success_message = {'message':message}
            return Response(success_message)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        #getting object by id
        apiview = 'get method by id'
        message = {'message':apiview}
        return Response(message)

    def update(self,request,pk=None):
        #only updates fields update ==  put
        apiview = 'update object method'
        message = {'message':apiview}
        return Response(message)

    def partial_update(self,request,pk=None):
        #partial_update == patch
        apiview = 'partial_update method'
        message = {'message':apiview}
        return Response(message)

    def destroy(self,request,pk=None):
        #destroy == delete
        apiview = 'destroy method'
        message = {'message':apiview}
        return Response(message)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)


class ProfileFeedItemViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticatedOrReadOnly)


    def perform_create(self, serializer):

        serializer.save(user_profile=self.request.user)
