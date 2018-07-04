class Query:

    @classmethod
    def count(cls, otherClass):
        return len(otherClass.all())

    @classmethod
    def find_by_name(cls, otherClass, name):
        name_list = [i for i in otherClass.all() if i.name == name]
        return name_list[0]

    @classmethod
    def name_starts_with(cls, otherClass, letter):
        return [object for object in otherClass.all() if object.name[0] == letter]

    @classmethod
    def is_older_than(cls, otherClass, age):
        name_list = [object for object in otherClass.all() if object.age > age]
        return name_list

    @classmethod
    def mean_age(cls, otherClass):
        age_list = [object['age'] for object in otherClass.all_ages()]
        return sum(age_list)/len(age_list)
