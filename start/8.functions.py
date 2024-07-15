def hello_world(value):
    print("hello world! " + str(value))


hello_world("Ok")


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return (num1 + num2)


total = sum(7, 2)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Krystian", 213, "Arek")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Marek", last="Adam")
