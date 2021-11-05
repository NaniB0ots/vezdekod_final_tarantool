import uuid

from pydantic import BaseModel


class Link(BaseModel):
    id: str
    original: str
    short: str

    def __init__(self, original: str, short: str, id: str = None):
        if not id:
            id = uuid.uuid4().hex
        super(Link, self).__init__(original=original, short=short, id=id)

    @property
    def data_to_save(self):
        return [self.id, self.original, self.short]
