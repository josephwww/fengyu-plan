from abc import ABC, abstractmethod


class DatabaseObject(ABC):
    @abstractmethod
    def update(self):
        pass


class Client(ABC):

    @abstractmethod
    def create(self, db_object: DatabaseObject):
        pass

    @abstractmethod
    def update(self, db_object_id, db_object: DatabaseObject):
        pass

    @abstractmethod
    def delete(self, db_object_id):
        pass

    @abstractmethod
    def get(self, db_object_id):
        pass

    @abstractmethod
    def list(self, start, limit, sort, direct, search):
        pass



