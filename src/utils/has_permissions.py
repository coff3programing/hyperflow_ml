""" Managing permissions """
from rest_framework.permissions import IsAdminUser, IsAuthenticated


def get_permission_classes(action):
    """
    Returns permission classes based on the action.
    - Only admins can 'create', 'update', or 'destroy'.
    - Any authenticated user can 'list' or 'retrieve'.
    """
    if action in ['create', 'update', 'destroy']:
        return [IsAdminUser]
    else:
        return [IsAuthenticated]


def get_permission_methods(method):
    """
    Returns permission classes based on the HTTP method.
    - Only admins can 'POST' (file upload).
    - Any authenticated user can 'GET' (list).
    """
    return [IsAdminUser] if method == 'POST' else [IsAuthenticated]
