import string
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        alphabet = string.ascii_letters

        if len(username) < 3:
            raise UserInputError("Username too short")

        user_only_letters = True
        for i in username:
            if i not in alphabet:
                user_only_letters = False

        if not user_only_letters:
            raise UserInputError("Username can be only letters a-z")
        
        if len(password) < 8:
            raise UserInputError("Password too short")
        
        only_letters = True
        fin_alphabet = string.ascii_letters+"åöäÅÖÄ"
        # print(alphabet)

        for i in password:
            if i not in fin_alphabet:
                only_letters = False
        
        if only_letters:
            raise UserInputError("Password can't be only letters")
        
        if password != password_confirmation:
            raise UserInputError("Passwords dont match")


user_service = UserService()
