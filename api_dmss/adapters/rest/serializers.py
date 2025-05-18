from rest_framework import serializers

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class CreateRoleSerializer(serializers.Serializer):
    name = serializers.CharField()

class AssignRoleSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    role_id = serializers.UUIDField()
