import uuid

from pydantic import BaseModel
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


class Link(BaseModel):
    id: str
    original: str
    short: str

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is list:
            kwargs['id'] = args[0][0]
            kwargs['original'] = args[0][1]
            kwargs['short'] = args[0][2]
            args = []

        if not kwargs.get('id'):
            kwargs['id'] = uuid.uuid4().hex
        if not kwargs.get('short'):
            kwargs['short'] = generate_random_string(8)
        super(Link, self).__init__(*args, **kwargs)

    @property
    def data_to_save(self):
        return [self.id, self.original, self.short]

    def generate_new_short(self):
        self.short = generate_random_string(8)
