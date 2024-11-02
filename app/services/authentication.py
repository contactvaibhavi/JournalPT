from schema.user import User


class AuthenticationService:
    def __init__(self) -> None:
        self.user = User(
            user_id=1,
            user_name="Jane Doe", 
            user_age=30
        )

    def get_user(self):
        return self.user
