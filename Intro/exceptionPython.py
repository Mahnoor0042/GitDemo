

ItemsInCart = 0

if ItemsInCart != 2:
    pass
    #raise Exception("Product cart count is not matching")
assert (ItemsInCart == 0)

try:
    with open('random.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print (e)
finally:
    print("cleaning up records")