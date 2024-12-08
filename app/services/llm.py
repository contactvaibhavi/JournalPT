from datetime import date
from sqlalchemy import desc, select
from  schema.ai_generated import AiGenerated
from  schema.entry import Entry
from  schema.llm_call import LlmCall
from services.db import DbSession
from openai import OpenAI

class LlmService:
    model = "gpt-4o-mini"
    summarise_system_prompt = "You are a journal summariser."
    summarise_user_prompt = "Summarise the following journal entries:"

    def __init__(self):
        self.db = DbSession()
        self.openai = OpenAI()

    def summarise_entrys(self, user_id: int, days: list[date]):
        query = select(Entry)\
                .where(Entry.user_id == user_id)\
                .where(Entry.date.in_(days))\
                .order_by(desc(Entry.date))
        entrys: list[Entry] = [row._asdict()["Entry"] for row in self.db.execute(query)]
        print(entrys)
        data = "\n".join([f'Date:{entry.date}\n{entry.content}' for entry in entrys])

        completion = self.openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.summarise_system_prompt},
                {"role": "user","content": self.summarise_user_prompt + "\n\n" + data}
            ]
        )
        
        call = LlmCall(
            user_id=user_id,
            model=completion.model,
            type="summarise",
            input_tokens=completion.usage.prompt_tokens if completion.usage else 0,
            output_tokens=completion.usage.completion_tokens if completion.usage else 0,
            meta={"id": completion.id}
        )
        self.db.add(call)
        content = completion.choices[0].message.content
        aigen = AiGenerated(
            user_id=user_id,
            llm_call_id=call.llm_call_id,
            type="summarise",
            entry_ids=[entry.entry_id for entry in entrys],
            content=content
        )
        self.db.add(aigen)
        self.db.commit()

        return aigen.to_dict()
    
    def get_aigen_by_id(self, aigen_id: int):
        query = select(AiGenerated).where(AiGenerated.aigenerated_id == aigen_id)
        doc = self.db.execute(query).first()
        if not doc:
            return None
        return doc._asdict()
    
    def get_llm_calls(self, limit: int, skip: int):
        query = select(LlmCall).limit(limit).offset(skip)
        return [row._asdict() for row in self.db.execute(query)]
        