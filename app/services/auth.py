from sqlalchemy import select
from services.db import DbSession
from schema.user import User
import bcrypt 

def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class AuthenticationService:
    def __init__(self):
        self.db = DbSession()

    def create_user(self, user_email: str, user_password: str, user_name: str, user_age: int):
        user_id = self.db.query(User.user_id).count()
        user = User(
            user_email=user_email,
            user_id=user_id, 
            user_name=user_name, 
            user_age=user_age,
            user_hash=hash_password(user_password)
        )
        self.db.add(user)
        self.db.commit()
        return user_id

    def get_user(self, user_email: str): 
        query = select(User).where(User.user_email == user_email)
        for row in self.db.execute(query):
            return row._asdict()
