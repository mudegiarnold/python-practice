def my_function():
    print("Hello from a function")

my_function()


def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)

    my_function("Emil", "Refsnes")


def my_function(*kids):
                print("The youngest child is " + kids[2])
                my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

