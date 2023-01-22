import random
result = []


def divider(a, b):
    try:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if int(a) < int(b):
            raise ValueError
        if int(b) > 100:
            raise IndexError
        return a
    except ValueError:
        print("?")
    except IndexError:
        print("?")
    finally:
        pass


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}


for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
