# import your Query class

from query import Query

class Person:

    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person._all.append(self)

    @classmethod
    def count(cls):
        return Query.count(cls)

    @classmethod
    def find_by_name(cls, name):
        return Query.find_by_name(cls, name)

    @classmethod
    def name_starts_with(cls, first_letter):
        return Query.name_starts_with(cls, first_letter)

    @classmethod
    def is_older_than(cls, age):
        return Query.is_older_than(cls, age)

    @classmethod
    def mean_age(cls):
        return Query.mean_age(cls)

    #decorators for _name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    #decorarors for _age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    #decorators for _age
