class Query:
    @classmethod
    def count(cls, cls_opperate):
        return len(cls_opperate.all())
    @classmethod
    def find_by_name(cls, cls_opperate, name):
        return [person for person in cls_opperate.all() if person.name == name][0]
    @classmethod
    def name_starts_with(cls, cls_opperate, chara):
        return [person for person in cls_opperate.all() if person.name[0].upper() == chara.upper()]
    @classmethod
    def is_older_than(cls, cls_opperate, age):
        return [person for person in cls_opperate.all() if person.age > age]
    @classmethod
    def mean_age(cls, cls_opperate):
        cls_age_list = [person.age for person in cls_opperate.all()]
        return sum(cls_age_list) / len(cls_age_list)
