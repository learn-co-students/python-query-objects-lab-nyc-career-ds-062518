# import your Query class here
from query import Query
class Person:
    _all = []

    def __init__(self, _name, _age):
        self._name = _name
        self._age = _age
        Person._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def count(cls):
        return Query.count(cls)

    @classmethod
    def find_by_name(cls, _name):
        return [item for item in cls._all if item._name == _name][0]

    @classmethod
    def name_starts_with(cls, _letter):
        return [item for item in cls._all if item._name.upper().startswith(_letter.upper())]

    @classmethod
    def is_older_than(cls, _age):
        return [item for item in cls._all if item._age > _age]

    @classmethod
    def mean_age(cls):
        all_ages = [item._age for item in cls._all]
        return sum(all_ages) / len(cls._all)
