from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name',
        required=False,  # Make groups optional
        allow_null=True,  # Allow null values
        default=[]
    )
    user_permissions = serializers.SlugRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        slug_field='codename',
        required=False,  # Make groups optional
        allow_null=True,  # Allow null values
        default=[]
    )

    class Meta:
        model = Client
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = Client.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data.pop('password'))
        user.groups.set([])
        user.user_permissions.set([])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        if 'groups' in validated_data:
            instance.groups.set(validated_data['groups'])
        if 'user_permissions' in validated_data:
            instance.user_permissions.set(validated_data['user_permissions'])
        instance.save()
        return instance