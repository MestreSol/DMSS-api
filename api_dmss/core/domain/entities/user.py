from dataclasses import dataclass


@dataclass
class User:
    """
    User entity class.

    Attributes:
        id (str): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """

    id: str
    name: str
    email: str
    password: str