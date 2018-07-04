class Query:

    @classmethod
    def count(cls, cls_operate):
        return len(cls_operate._all)

    @classmethod
    def find_by_name(cls, cls_operate, name):
        for person in cls_operate._all:
            if person._name == name:
                return person

    @classmethod
    def name_starts_with(cls, cls_operate, letter):
        return [person for person in cls_operate.all() if person._name.startswith(letter)]

    @classmethod
    def is_older_than(cls, cls_operate, number):
        return [person for person in cls_operate.all() if person._age>number]

    @classmethod
    def mean_age(cls, cls_operate):
        age_list = [person._age for person in cls_operate.all()]
        total = sum(age_list)
        return total/len(age_list)
