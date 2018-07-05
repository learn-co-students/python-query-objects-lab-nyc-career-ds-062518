class Query:

    @classmethod
    def count(cls, otherClass):
        return len(otherClass.all())

    @classmethod
    def find_by_name(cls, otherClass, name):
        for person in otherClass.all():
            if person.name == name:
                return person
    @classmethod
    def name_starts_with(cls, otherClass, letter):
        initial_list= []
        for initial in otherClass.all():
            if initial.name.startswith(letter):
                initial_list.append(initial)
        return initial_list

    @classmethod
    def is_older_than (cls, otherClass, age):
        older_list = []
        for old in otherClass.all():
            if old.age > age:
                older_list.append(old)
        return older_list

    @classmethod
    def mean_age (cls, otherClass):
        people = otherClass.all()
        num_people = len(otherClass.all())
        age_list = (person.age for person in people)
        total_age = sum(age_list)/num_people
        return total_age
