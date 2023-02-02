import random as r
from datetime import datetime


def First_function(number):
    def First_function(*args, **kwargs):
        result = number(*args, **kwargs)
        a = r.randint(1,10)
        if a == result:
            print("You win")
        else:
            print("You looser")
    return First_function

@First_function

def second_function():
    try:
        start_time = datetime.now()
        First_function(int(input("Enter any digit \n")))
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
    except ValueError:
        print("You must enter digit")
    except IndexError:
        print("IndexError")
