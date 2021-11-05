import tarantool
import models


class Store:
    def __init__(self):
        self.connection = tarantool.connect('localhost', 3301)

        self.tester = self.connection.space('link')

    def get_space(self, space_name: str):
        return self.connection.space(space_name)

    def get_link(self, pk: str):
        pk = str(pk)
        data = self.tester.select(pk)
        if len(data) == 1:

            return models.Link(data[0])
        elif len(data) == 0:
            return {}
        else:
            return {}

    def create_link(self, instance: models.Link):
        for _ in range(5):
            try:
                self.tester.insert(instance.data_to_save)
                return instance
            except tarantool.error.DatabaseError:
                instance.generate_new_short()
                continue
        raise tarantool.error.DatabaseError("Can't create unique short link")
