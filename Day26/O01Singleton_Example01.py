
class Subject:

    __shared_subject = dict()

    def __init__(self):
        self.__dict__ = self.__shared_subject
        self.subject = "Mathmetics"

    def __str__(self):
        return self.subject

if __name__ == '__main__':
    prof1 = Subject()
    prof2 = Subject()
    prof3 = Subject()

    prof1.subject = "Data Science"
    prof2.subject = "Statistics"
    prof3.subject = "Python"

    print(prof1)
    print(prof2)
    print(prof3)

    print(prof1.__dict__)
    print(prof2.__dict__)
    print(prof3.__dict__)

