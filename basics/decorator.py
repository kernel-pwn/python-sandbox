# A function that extends the behavior of anther function
# w/o modifying the bas function
# pass the base function as an argument  to the decorator

# @add_sprinkles
# get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"here is your {flavor} of ice cream")

get_ice_cream("vanilla")