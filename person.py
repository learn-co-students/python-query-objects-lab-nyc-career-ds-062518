# import your Query class here
from query import Query

class Person:
    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def count(cls):
        return len(cls.all())

    @classmethod
    def find_by_name(cls, name):
        for person in Person.all():
            if person._name == name:
                return person

    @classmethod
    def name_starts_with(cls, letter):
        return [person for person in cls.all() if person._name.startswith(letter)]

    @classmethod
    def is_older_than(cls, number):
        return [person for person in cls.all() if person._age>number]

    @classmethod
    def mean_age(cls):
        age_list = [person._age for person in cls.all()]
        total = sum(age_list)
        return total/len(age_list)



    # @property
    # def age(self):
    #     return self._age
    #
    # @age.setter
    # def age(self, age):
    #     self._age = age

    pass
