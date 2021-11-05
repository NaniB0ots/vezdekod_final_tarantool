import tarantool
import models


def serialise(space_data) -> dict:
    print(space_data[0])
    return {
        space_data[0]: {
            'name': space_data[1],
            'birthday': space_data[2],
        }
    }


class Store:
    def __init__(self):
        self.connection = tarantool.connect('localhost', 3301)

        self.tester = self.connection.space('link1')



    def get_space(self, space_name: str):
        return self.connection.space(space_name)

    def get_link(self, pk: int):
        pk = int(pk)
        data = self.tester.select(pk)
        if len(data) == 1:

            return models.Link(data[0])
        elif len(data) == 0:
            return {}
        else:
            return {}
