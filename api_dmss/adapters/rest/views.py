from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from usecases.users.create_user import CreateUser
from usecases.users.assign_role import AssignRole
from usecases.roles.create_role import CreateRole

from adapters.persistence.user_repo_django import DjangoORMUserRepository
from adapters.persistence.role_repo_django import DjangoORMRoleRepository
from adapters.rest.serializers import (
    CreateUserSerializer,
    CreateRoleSerializer,
    AssignRoleSerializer
)

class CreateUserView(APIView):
    def post(self, request):
        ser = CreateUserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        usecase = CreateUser(repo=DjangoORMUserRepository())
        user = usecase.execute(**ser.validated_data)
        return Response({
            "id": str(user.id),
            "username": user.username,
            "email": user.email,
        }, status=status.HTTP_201_CREATED)

class CreateRoleView(APIView):
    def post(self, request):
        ser = CreateRoleSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        usecase = CreateRole(repo=DjangoORMRoleRepository())
        role = usecase.execute(**ser.validated_data)
        return Response({
            "id": str(role.id),
            "name": role.name,
        }, status=status.HTTP_201_CREATED)

class AssignRoleView(APIView):
    def post(self, request):
        ser = AssignRoleSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        usecase = AssignRole(
            user_repo=DjangoORMUserRepository(),
            role_repo=DjangoORMRoleRepository()
        )
        user = usecase.execute(**ser.validated_data)
        return Response({
            "id": str(user.id),
            "role_id": str(user.role_id),
        }, status=status.HTTP_200_OK)
