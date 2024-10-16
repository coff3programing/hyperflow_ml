""" Imports """
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view as app
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    authentication_classes,
    permission_classes
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer


@app(['POST'])
def login(request):
    """ Login """
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'message': 'Invalid Password'},
                        status=status.HTTP_400_BAD_REQUEST)

    # Eliminar el token actual si existe
    Token.objects.filter(user=user).delete()

    # Crear un nuevo token
    token = Token.objects.create(user=user)

    serializer = UserSerializer(instance=user)
    context = {'token': token.key, 'user': serializer.data}
    return Response(context, status=status.HTTP_200_OK)


@app(['POST'])
def register(request):
    """ Register """
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        context = {'token': token.key, 'username': serializer.data}
        return Response(context, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@app(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    """ Profile """
    print(request.user)
    context = {
        'username': request.user.username,
        'email': request.user.email,
        # 'token': Token.objects.get(user=request.user).key
    }
    return Response(context, status=status.HTTP_200_OK)


@app(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    """ Logout """
    # Eliminar el token actual del usuario para cerrar sesión
    Token.objects.filter(user=request.user).delete()
    return Response({'message': 'Successfully logged out'},
                    status=status.HTTP_200_OK)
