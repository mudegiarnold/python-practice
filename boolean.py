print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
    def  __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True

print(myFunction())

