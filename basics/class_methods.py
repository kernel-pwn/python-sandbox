# allow operations related to the class itself
# take (cls/self) as the first parameter, which responds the class itself

class student():

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa

    # instance
    def get_info(self):
        return f'{self.name} {self.gpa}'

    @classmethod
    def get_count(cls):
        return f"total students {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"{student.total_gpa/cls.count:.2f}"

student1 = student("spongebob", 3.2)
student2 = student("patrick", 2.0)
student3 = student("sandy", 4.0)


print(student.get_count())
print(student.get_average_gpa())