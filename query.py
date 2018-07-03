class Query:

    @classmethod
    def count(cls, queriedclass):
        return len(queriedclass.all())

    @classmethod
    def find_by_name(cls, queriedclass, name):
        return [pers for pers in queriedclass.all() if pers._name == name][0]

    @classmethod
    def name_starts_with(cls, queriedclass, firstletter):
        return [pers for pers in queriedclass.all() if pers._name[0] == firstletter]

    @classmethod
    def is_older_than(cls, queriedclass, cutoffage):
        return [pers for pers in queriedclass.all() if pers._age > cutoffage]

    @classmethod
    def mean_age(cls, queriedclass):
        return round(sum([pers._age for pers in queriedclass.all()]) / cls.count(queriedclass), 2)
