from sqlalchemy import select
from services.db_service import DbService
from schema.user import User


class AuthenticationService:
    def get_user(self, user_id: int): 
        query = select(User).where(User.user_id == user_id)
        db_service = DbService()
        db_service.create_db()
        assert db_service.engine is not None
        with db_service.engine.connect() as connection:
            for row in connection.execute(query):
                return row._asdict()
