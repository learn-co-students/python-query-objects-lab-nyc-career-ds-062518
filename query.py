class Query:
    @classmethod
    def count(cls, OtherClass):
        return len(OtherClass._all)

    @classmethod
    def find_by_name(cls, OtherClass, name):
        return [item for item in OtherClass._all if item._name == name][0]

    @classmethod
    def name_starts_with(cls, OtherClass, letter):
        upper_letter = letter.upper()
        return [item for item in OtherClass._all if item._name.upper().startswith(upper_letter)]

    @classmethod
    def is_older_than(cls, OtherClass, age):
        return [item for item in OtherClass._all if item._age > age]

    @classmethod
    def mean_age(cls, OtherClass):
        all_ages = [item._age for item in OtherClass._all]
        return (sum(all_ages))/(len(OtherClass._all))
