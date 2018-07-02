class Query:

    @classmethod
    def count(cls, OtherClass):
        return len(OtherClass._all)

    @classmethod
    def find_by_name(cls, OtherClass, _name):
        return [item for item in OtherClass._all if item._name == _name][0]

    @classmethod
    def name_starts_with(cls, OtherClass, _letter):
        return [item for item in OtherClass._all if item._name.upper().startswith(_letter.upper())]

    @classmethod
    def is_older_than(cls, OtherClass, _age):
        return [item for item in OtherClass._all if item._age > _age]

    @classmethod
    def mean_age(cls, OtherClass):
        all_ages = [item._age for item in OtherClass._all]
        return sum(all_ages) / len(OtherClass._all)
