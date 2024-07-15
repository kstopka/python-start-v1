name = "Krystian"
count = 1
print()
print(name)


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(name)
        print(color)

    greeting("Eryk")


another()
