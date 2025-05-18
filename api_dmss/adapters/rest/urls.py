from django.urls import path
from adapters.rest.views import (
    CreateUserView, CreateRoleView, AssignRoleView
)

urlpatterns = [
    path("users/",    CreateUserView.as_view(),  name="create-user"),
    path("roles/",    CreateRoleView.as_view(),  name="create-role"),
    path("assign/",   AssignRoleView.as_view(),  name="assign-role"),
]
