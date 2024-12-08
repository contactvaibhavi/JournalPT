import datetime
from typing import Union

from sqlmodel import select, desc
from services.db import DbSession
from schema.entry import Entry

class JournalService:
    def post_entry(self, user_id: int, content: str, date: Union[datetime.date, None]) -> int:
        if date is None:
            date = datetime.date.today()
        timestamp=datetime.datetime.now()
        db = DbSession()

        entry_id = db.query(Entry.entry_id).count()
        entry = Entry(
            entry_id=entry_id,
            user_id=user_id,
            content=content,
            date=date,
            timestamp=timestamp
        )
        db.add(entry)

        db.commit()
        return entry_id

    def get_entrys_by_user_id(self, user_id: int):
        query = select(Entry).where(Entry.user_id == user_id).order_by(desc(Entry.date))
        return [row._asdict() for row in DbSession().execute(query)]