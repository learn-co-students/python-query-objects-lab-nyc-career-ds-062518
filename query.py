class Query:

    @classmethod
    def count(cls, otherClass):
        count = 0
        for item in otherClass._all:
            count += 1
        return count

    @classmethod
    def find_by_name(cls, otherClass, name):
        for item in otherClass._all:
            if item._name == name:
                return item

    @classmethod
    def name_starts_with(cls, otherClass, first_letter):
        name_starts_with = []
        for item in otherClass._all:
            if item._name.startswith(first_letter):
                name_starts_with.append(item)
        return name_starts_with

    @classmethod
    def is_older_than(cls, otherClass, age):
        oldies = []
        for item in otherClass._all:
            if item._age > age:
                oldies.append(item)
        return oldies

    @classmethod
    def mean_age(cls, otherClass):
        all_ages = [item._age for item in otherClass._all]
        mean_age = sum(all_ages)/len(all_ages)
        return mean_age
