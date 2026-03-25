from collections.abc import Iterator

def add_matter4(cls):
    original_init = cls.__init__

    def new_init(self, name, m1, m2, m3, m4=0):
        original_init(self, name, m1, m2, m3)
        self.m4 = m4

    cls.__init__ = new_init
    return cls


@add_matter4
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
    
class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.m2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.m3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student
    
class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.m4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.m1, reverse=True)
    
    def rank_matter_2(self):
        return sorted(self.students, key=lambda s: s.m2, reverse=True)

    def rank_matter_3(self):
        return sorted(self.students, key=lambda s: s.m3, reverse=True)
    
    def __iter__(self):
        return iter(self.rank_matter_1())
    
    def iter_matter_2(self):
        return Matter2Iterator(self.students)

    def iter_matter_3(self):
        return Matter3Iterator(self.students)
    
    def iter_matter_4(self):
        return Matter4Iterator(self.students)
    
    


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    print(school_class.rank_matter_1())
    print(school_class.rank_matter_2())
    print(school_class.rank_matter_3())
    
    for s in school_class:
        print(s.name)

    for s in school_class.iter_matter_2():
        print(s.name)

    for s in school_class.iter_matter_3():
        print(s.name)
    
    s = Student('Test', 10, 10, 10, 15)
    print(s.m4)


    for s in school_class.iter_matter_4():
        print(s.name)