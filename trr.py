import random as r
from datetime import datetime


def First_function(eger):
    def Decorator(*args, **kwargs):
        try:
            eger = int(*args, **kwargs)
            a = r.randint(1,10)
            if a == eger:
                print("You win")
            else:
                print("You looser")
        except ValueError:
            print("You must print digit")
        except IndexError:
            print("IndexError")
        finally:
            pass
    return Decorator


def second_function():
    start_time = datetime.now()
    First_function(input("Enter any digit \n"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


second_function()