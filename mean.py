"""
Example Python Module for basic testing.
"""

def mean(num_list):
    """
    Calculates mean of a list
    :param num_list: list of numbers
    """
    assert len(num_list) != 0
    return sum(num_list) / len(num_list)


def mean_exc(num_list):
    if len(num_list) == 0 :
      raise Exception("The algebraic mean of an empty list is undefined.\
      	    	       Please provide a list of numbers")
    else :
      return sum(num_list)/len(num_list)

def mean_try(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined. Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)

def mean_try_again(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)

def main():
    """
    Simple check of mean(num_list):
    calls mean on:
    numbers = [1, 2, 3, 4, 5],
    returning the mean, 3.0
    nonumbers = []
    which causes an assertion error due to passing an empty list
    """

    numbers = [1, 2, 3, 4, 5]

    print(mean(numbers))

    nonumbers = []

    print(mean(nonumbers))

if __name__ == '__main__':
    main()

