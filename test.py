
import random as r
from datetime import datetime


def First_function(a=r.randint(1, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)):
    try:
        b = int(input("Print any digit \n"))
        if a == b:
            print("You win")
        else:
            print("You looser")
    except ValueError:
        print("You must print digit")
    except IndexError:
        print("IndexError")
    finally:
        pass

def second_function():
    start_time = datetime.now()
    First_function()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

