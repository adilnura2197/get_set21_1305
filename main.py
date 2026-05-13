class University:
    def __init__(self, name, students):
        self.name = name
        self.__students = students

    def get_students(self):
        return self.__students

    def set_students(self, new_students):
        self.__students = new_students


u1 = University('TATU', 12000)

print(u1.name)
print(u1.get_students())

u1.set_students(15000)

print(u1.get_students())
