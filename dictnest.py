myfamily = {
        "child1" : {
            "name" : "Emil",
            "year" : 2004
            },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
            },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
            }
        }
print(myfamily)


print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

