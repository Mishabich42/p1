# Task 1
""""
my_iterable = iter([i for i in range(1000)])

for item in my_iterable:
    print(next(my_iterable))

"""


# Task 2

def calculate(expression):
    def calculate(*args, **kwargs):
        try:
            result = int(expression(*args, **kwargs))
        except ValueError:
            print("You must enter digit")
        except IndexError:
            print("IndexError")
        except ZeroDivisionError:
            print("Сannot be divided by 0")
        except SyntaxError:
            print("You must enter (+, -, *, /)")
        except TypeError:
            print("You must enter (+, -, *, /)")
        except NameError:
            print("You must enter digit")
        else:
            print(result)

    return calculate


@calculate
def caluculater(exprassion):
    return eval(exprassion)


caluculater(input(""))
