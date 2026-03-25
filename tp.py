class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3


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


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    print(school_class.rank_matter_1())
    print(school_class.rank_matter_2())
    print(school_class.rank_matter_3())