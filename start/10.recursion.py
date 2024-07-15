import random
# def add_one(num):
#     if (num >= 9):
#         print("here")
#         return num + 1

#     total = num + 1
#     print(total)

#     return add_one(total)


# mynewtotal = add_one(0)
# print(mynewtotal)


def getrandomnum(i, value=0):
    random_num = random.randint(1, 10)
    if (random_num == 5):
        if (value >= 100):
            print("version: " + str(value) + " and "+str(i))
            return
        return
    value += 1
    getrandomnum(i, value)


for i in range(100000):
    isOk = getrandomnum(i)
