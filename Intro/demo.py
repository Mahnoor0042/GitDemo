print("good morning")

a = 100
print("value", a, "is", type(a))
values = [1, 2, 3, "hello"]
print(values[2])
values.insert(2, "hehe")
print(values[2])
values.insert(4, "test")


it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 4:
        break
    print(it)
    it = it - 1
