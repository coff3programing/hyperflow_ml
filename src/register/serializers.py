""" URLS """
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """
    class Meta:
        """ Config """
        model = User
        fields = ['username', 'email', 'password']
