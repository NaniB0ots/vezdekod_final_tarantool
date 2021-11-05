from pydantic import BaseModel


class Link(BaseModel):
    id: int
    original: str
    short: str

    def __init__(self, *args, **kwargs):
        print(args, )
        print(kwargs)
        if args and type(args[0]) is list:
            kwargs = {
                'id': args[0][0],
                'original': args[0][1],
                'short': args[0][2]
            }
            args = args[1:]
        print(args, kwargs)
        super(Link, self).__init__(*args, **kwargs)
