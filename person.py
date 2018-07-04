from query import * # import your Query class here
class Person:
    _all = []
    _allnames = []
    _count = 0

    def __init__ (self, name, age):
        self._name= name
        self._age= age
        Person._count += 1
        Person._allnames.append(self._name)
        Person._all.append(self)

    @property
    def name(self):
        return self._name
    @property
    def age (self):
        return self._age
    @classmethod
    def all(cls):
        return cls._all
    @classmethod
    def allnames(cls):
        return cls._allnames
    @classmethod
    def count(cls):
        return Query.count(cls)
    @classmethod
    def find_by_name(cls, name):
        return Query.find_by_name(cls, name)
    @classmethod
    def name_starts_with(cls, initial):
        return Query.name_starts_with (cls, initial)
    @classmethod
    def is_older_than(cls, age):
        return Query.is_older_than(cls, age)
    @classmethod
    def mean_age(cls):
        return Query.mean_age(cls)
