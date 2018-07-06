class Query:

    def count(cls):
        return len(cls._all)

    def find_by_name(cls, name):
        for per in cls._all:
            if per._name == name:
                return per
            else:
                return "There is no person with name " + name

    def name_starts_with(cls, letter):
        return [info for info in cls._all if info._name.startswith(letter)]

    def is_older_than(cls, num):
        return [person for person in cls.all() if person._age > num]

    def mean_age(cls):
        age_tot = 0
        for old in cls.all():
            age_tot += old.age
        return age_tot/len(cls._all)
