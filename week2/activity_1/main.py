# a basic import
from greeter import calculator

calc1 = calculator(30, 40)

print(calc1.sum())
print(calc1.subtraction())
print(id(calc1))

def modify(n, list_):
    n = 2
    list_.append(3)
    print(n)

n = 1
list_ = [1,2]
modify(n, list_)
print(n)
print(list_)

def modify_list(list_):
    list_.append("new")
    list_ = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)

# use an alias - consider why might we do this?

# sometimes we only want to import what we need

# create a calculator class in the module

# use the new class to return a score to a user



