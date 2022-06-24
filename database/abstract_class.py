from abc import ABC, abstractmethod


class DatabaseObject(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        """
        重写此方法用来格式化输出类的字符串
        :return:
        """
        pass

    @abstractmethod
    def __contains__(self, item):
        """
        重写此方法用来类的关键字搜索
        :param item:
        :return:
        """
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



