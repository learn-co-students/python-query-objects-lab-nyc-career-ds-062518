class Query:

    @classmethod
    def find_by_name(cls, otherClass, name):
        for object in otherClass.all():
            if object.name == name:
                return object
            else:
                return 'there is no one named {}' .format(name)

    @classmethod
    def count (cls, otherClass):
        totalcount= len(otherClass.all())
        return totalcount

    @classmethod
    def name_starts_with (cls, otherClass, initial):
        return [object for object in otherClass.all() if object.name.startswith(initial)]

    @classmethod
    def is_older_than(cls, otherClass, age):
        return [object for object in otherClass.all() if object.age > age]

    @classmethod
    def mean_age(cls, otherClass):
        totalcount= len(otherClass.all())
        list_of_ages=[object.age for object in otherClass.all()]
        combined_ages=sum(list_of_ages)
        meanage = combined_ages / totalcount
        return  meanage
