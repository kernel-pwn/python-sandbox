# An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

# 1/0     # 1 + "1"     # int("pizza")

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("enter a number")
except exception:
    print("something is wrong")
finally:
    print("do some cleanup")