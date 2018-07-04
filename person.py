from query import Query

class Person:

    _all = []
    _all_ages = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person._all.append(self)
        Person._all_ages.append({'age': age, 'name': name})

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def all_ages(cls):
        return cls._all_ages

    @classmethod
    def count(cls):
        return Query.count(cls)

    @classmethod
    def find_by_name(cls, name):
        return Query.find_by_name(cls, name)

    @classmethod
    def name_starts_with(cls, letter):
        return Query.name_starts_with(cls, letter)

    @classmethod
    def is_older_than(cls, age):
        return Query.is_older_than(cls, age)

    @classmethod
    def mean_age(cls):
        return Query.mean_age(cls)
