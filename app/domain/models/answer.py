from pydantic import BaseModel


class Answer(BaseModel):
    reason: str
