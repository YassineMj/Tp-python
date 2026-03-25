from collections.abc import Iterable, Iterator

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
    
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class SchoolClass(Iterable):
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

    print("\n--- Classement en Mathématiques ---")
    for s in school_class.rank_matter_1():
        print(f"{s.name} : {s.m1}")

    print("\n--- Classement en Physique ---")
    for s in school_class.rank_matter_2():
        print(f"{s.name} : {s.m2}")

    print("\n--- Classement en Informatique ---")
    for s in school_class.rank_matter_3():
        print(f"{s.name} : {s.m3}")

    print("\n--- Classement Général (Moyenne) ---")
    students_sorted = sorted(school_class.students, key=lambda s: s.average(), reverse=True)
    for s in students_sorted:
        print(f"{s.name} : {s.average():.2f}")

    print("\n--- Parcours via l'itérateur (Matière 1) ---")
    for s in school_class:
        print(f"{s.name} : {s.m1}")

    print("\n--- Parcours via l'itérateur (Matière 2) ---")
    for s in school_class.iter_matter_2():
        print(f"{s.name} : {s.m2}")

    print("\n--- Parcours via l'itérateur (Matière 3) ---")
    for s in school_class.iter_matter_3():
        print(f"{s.name} : {s.m3}")

    print("\n--- Vérification de la 4ème matière ajoutée par le décorateur ---")
    s1 = Student('J', 10, 12, 13, 10)
    s2 = Student('A', 8, 2, 17, 10)
    s3 = Student('V', 9, 14, 14, 10)

    print(f"{s1.name} a {s1.m4} en Anglais. (Moyenne: {s1.average():.2f})")
    print(f"{s2.name} a {s2.m4} en Anglais. (Moyenne: {s2.average():.2f})")
    print(f"{s3.name} a {s3.m4} en Anglais. (Moyenne: {s3.average():.2f})")

    print("\n--- Parcours via l'itérateur injecté (Matière 4 - Anglais) ---")
    for s in school_class.iter_matter_4():
        print(f"{s.name} : {s.m4} en Anglais")

    print("\n--- Vérification du Singleton ---")
    sc1 = SchoolClass()
    sc2 = SchoolClass()
    print("Les deux instances sont-elles identiques ?", sc1 is sc2)
    print("Nombre d'élèves dans la 'nouvelle' instance :", len(sc2.students))