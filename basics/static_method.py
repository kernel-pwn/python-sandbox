# A method that belong to a class rather than any object from that class (instance)
# usually used for general utility functions

# instance methods = best for operations on instances of the class (objects)
# static method = best for utility functions that do not need access to class data

class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cashier", "cook", "janitor"]
        return position in valid_positions

employee1 = employee("eugene", "manager")
employee2 = employee("squidward", "cashier")
employee3 = employee("spongebob", "cook")

print(employee.is_valid_position("manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())