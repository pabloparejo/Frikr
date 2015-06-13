#encoding:UTF-8
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from photos.models import Photo
from photos.permissions import UserPermission
from photos.views_queryset import PhotoQueryset
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers import UserSerializer, PhotoSerializer, PhotoListSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets



class UserViewSet(viewsets.ViewSet):
    permission_classes = (UserPermission,)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Detail
    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListDetailViewSet(object):
    list_serializer_class = None

    def get_serializer_class(self):
        LIST = (self.action.upper() == "LIST")
        return self.list_serializer_class if LIST else self.serializer_class


class PhotoViewSet(PhotoQueryset, ListDetailViewSet, viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    list_serializer_class = PhotoListSerializer
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ('name', 'owner', 'created_on')
    search_fields = ('name', 'description', 'owner__first_name', 'owner__last_name',)

    def perform_create(self, serializer):
        """
        Tras validar datos, antes de guardar se llama a este método
        """
        serializer.save(owner=self.request.user)
