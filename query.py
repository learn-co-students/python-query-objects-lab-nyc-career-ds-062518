class Query:
    @classmethod
    def count(cls, other_cls):
        return len(other_cls.all())

    @classmethod
    def find_by_name(cls, other_cls, name):
        for item in other_cls.all():
            if item._name == name:
                return item

    @classmethod
    def name_starts_with(cls, other_cls, letter):
        list_of_people = []
        for item in other_cls.all():
            if item._name[0] == letter:
                list_of_people.append(item)
        return list_of_people

    @classmethod
    def is_older_than(cls, other_cls, age):
        return [item for item in other_cls.all() if item._age > age]

    @classmethod
    def mean_age(cls, other_cls):
        all_age = [item._age for item in other_cls.all()]
        return round(sum(all_age)/len(all_age),0)
