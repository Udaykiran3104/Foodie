import os
import json
from shop.exceptions import FoodieExit
from shop.models import User
import peewee as pwee


class UserSession:
    """
    UserSession class saves the current logged in user in a session file
    and loads it when needed to avoid multiple logins for each command.
    """

    session_file = "./foodie.session"

    def __init__(self):
        self.current_user = None

    def __enter__(self):
        if os.path.exists(self.session_file):
            with open(self.session_file, "r") as file:
                session_data = json.load(file)
                self.current_user = session_data.get("current_user")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        session_data = {"current_user": self.current_user}
        with open(self.session_file, "w") as file:
            json.dump(session_data, file)
        self.current_user = None

    def set_current_user(self, user):
        # set current user to session
        self.current_user = user


class AuthenticationService:
    user = None

    def __init__(self, session: UserSession) -> None:
        self.session = session

    def list_users(self):
        users = User.select()
        for i, u in enumerate(users):
            print(f"{i+1}. {u.user_name}")

    def is_authenticated(self):
        if self.session.current_user is None:
            raise FoodieExit("User is not logged in.")

    def signup(self, user_name: str, password: str):
        try:
            user = User.create(user_name=user_name, password=password)
        except pwee.IntegrityError as e:
            raise FoodieExit(f"User '{user_name}' already exists.") from e

    def login(self, user_name: str, password: str):
        try:
            user = User.get(user_name=user_name, password=password)
            self.session.set_current_user(user.user_name)
        except pwee.DoesNotExist as e:
            raise FoodieExit("Check username and password") from e

    def load_session(self):
        if self.session.current_user is not None:
            self.user = User.get(user_name=self.session.current_user)
            try:
                self.user = User.get(user_name = self.session.current_user)
            except:
                print("something went wrong, login again.")
    

    def logout(self):
        with self.session:
            print(
                f"Thank you for using our application, {self.session.current_user}! See you soon, bye."
            )
