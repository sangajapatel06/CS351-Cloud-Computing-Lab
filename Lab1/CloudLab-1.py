import functools
from typing import List
import random
from operator import mul
from functools import reduce

# Problem 1

print("------ Q1 ------")


def split(word: str) -> List[str]:  # Problem 1
    """Return the  list of characters formed by breaking the string Name.

    doctests:
    >>> split("Word")
    ['W', 'o', 'r', 'd']
    >>> split("abc")
    ['a', 'b', 'c']
    """
    charList = list(word)
    return charList

# Problem 2


print("------ Q2 ------")


def join(word_list: List[str]) -> str:  # Problem 2
    """Returns a string after joining the character in the string list word_list.

    doctests:
    >>> join(['W', 'o', 'r', 'd'])
    'Word'
    >>> join (['a', 'b', 'c'])
    'abc'
    """
    word = "".join(word_list)
    return word


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")


print("\n------ Q3 ------")


def randomList(num: int) -> List[int]:  # Problem 3
    """Returns a list of n random numbers where n being the int num.

    doctests:
    >>> randomList(1)
    [1]
    >>> randomList(0)
    []
    """
    number_list = random.sample(range(1, num + 1), num)
    return number_list


if __name__ == "__main__":
    numbers = randomList(5)
    print(numbers)


# Problem 4

print("\n------ Q4 ------")


def descOrder(numList: List[int]) -> List[int]:  # Problem 4
    """Returns a sorted list of descending order from the given list numList.

    doctests:
    >>> descOrder([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]

    >>> descOrder([3, 4, 1, 2, 5])
    [5, 4, 3, 2, 1]

    """
    new_NumList = sorted(numList, reverse=True)
    return new_NumList


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="sorting", verbose=True)


# Problem 5

print("\n------ Q5 ------")


def freq(numbers: list) -> dict:
    """Count the elements in the dictionary
    doctests:
    >>> freq([1,1,3,2,3,2,3,2,2])
    {1: 2, 3: 3, 2: 4}
    >>> freq([])
    {}"""
    dictionary = dict()
    for x in numbers:
        dictionary[x] = dictionary.get(x, 0) + 1
    return dictionary


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")

# Problem 6


print("\n------ Q6 ------")


# Problem 6
def unique(numList: List[int]) -> set():
    """
    Function to get all the unique elements from given list.

    doctests:
    >>> unique([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> unique([1, 4, 9, 4, 4, 1, 1])
    {1, 4, 9}

    """
    s = set()
    for num in numList:
        s.add(num)  # set contains unique value

    return s


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")


# Problem7
print("\n------ Q7 ------")


def firstRepeatingEle(numList: List[int]) -> set():  # Problem 7
    """Returns the first repeating element from the given list numList.

    doctests:
    >>> firstRepeatingEle([1, 2, 3, 4, 5, 1, 2])
    {1}
    >>> firstRepeatingEle([1, 2, 5, 4, 5, 1])
    {5}
    """
    min = 10000000
    repeatingSet = set([0])
    for i in range(len(numList)):
        for j in range(i + 1, len(numList)):
            if numList[i] == numList[j]:
                if j - i < min:
                    repeatingSet.pop()
                    min = j - i
                    repeatingSet.add(numList[i])

    return repeatingSet


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")

# Problem 8

print("\n------ Q8 ------")

# n = int(input())

# function for making dictionary


def dictionary_formation(n: int) -> dict:
    """map indexes of a number to its squares and cubes

    doctests:
    >>> dictionary_formation(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> dictionary_formation(4)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64]}
    """
    Dict = {}
    for i in range(n + 1):
        Dict[i] = [i * i, i * i * i]
    return Dict


# print(dictionary_formation(n))
if __name__ == "__main__":
    import doctest

    doctest.testmod(name="dicionary_formation", verbose=True)

# Problem 9

print("\n------ Q9 ------")


def zipList(list1: list, list2: list) -> list:
    """map same indexes of two list into tuples
    doctests:
    >>> zipList([1, 2, 3, 4] , ['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> zipList(["name","age"],["Sangaja",21]) 
    [('name', 'Sangaja'), ('age', 21)]"""
    mapped = zip(list1, list2)
    return list(mapped)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")

# Problem 10

# print("\n------ Q10 ------")


# # n = int(input())

# # function for square list
# def square_list_formation(n: int) -> list:
#     """squaring elements in a list

#     doctests:
#     >>> square_list_formation(3)
#     [0, 1, 4, 9]
#     >>> square_list_formation(4)
#     [0, 1, 4, 9, 16]
#     """
#     x = [i * i for i in range(n + 1)]
#     #     print(x)
#     return x


# # square_list_formation(n)
# if __name__ == "__main__":
#     import doctest

#     doctest.testmod(name="square_list_formation", verbose=True)


def generateSqDC(num: int) -> List[int]:  # Problem 11
    """Returns a dictionary  mapping squares from 0 to n using dictionary comprehension.
    >>> generateSqDC(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> generateSqDC(10)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    newDict = {x: x ** 2 for x in range(num + 1)}
    return newDict


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")


# Problem 11


print("\n------ Q11 ------")


def squares(n: int) -> dict:
    """map indexes of a number to its squares
    doctests:
    >>> squares(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> squares(2)
    {0: 0, 1: 1, 2: 4}"""
    my_Dict = {x: x*x for x in range(n+1)}
    return dict(my_Dict)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")


# Problem 12

print("\n------ Q12 ------")


# def sq(x):
#     return x ** 2

def addtwo(x): return x + 2


class MyClass:
    # this function is to save i/p atomic values in an instance variable
    def __init__(self, input_list):
        self.input_list = input_list

    def __apply__(self) -> list:
        """applying function to input_list

        doctests:
        >>> input_list = [1, 4, 3, 4, 5]
        >>> c1 = MyClass(input_list)
        >>> c1.__init__(input_list)
        >>> print(c1.__apply__())
        [3, 6, 5, 6, 7]
        >>> input_list = ['a', 'b', 'c']
        >>> c2 = MyClass(input_list)
        >>> c2.__init__(input_list)
        >>> print(c2.__apply__())
        Oops! it was unvaild. Plz Try again...
        """
        try:
            listOfLambdas = [addtwo(i) for i in self.input_list]
            self.input_list = listOfLambdas
            return listOfLambdas
        except TypeError:
            str = "Oops! it was unvaild. Plz Try again..."
            return str


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="__apply__", verbose=True)


# Problem 13

print("\n------ Q13 ------")
# Problem 13


def upperCase(word: str) -> str:
    return word.upper()


def upperCaseList(wordList: List[str]) -> List[str]:
    """
    Function takes as input a list of words and upper-cases each word.

    doctests:
    >>> upperCaseList(['aa','bb','cd','e'])
    ['AA', 'BB', 'CD', 'E']
    >>> upperCaseList(['python'])
    ['PYTHON']

    """
    map_list = list(map(upperCase, wordList))

    return map_list


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="combine", verbose="True")


# Problem 14

print("\n------ Q14 ------")


# input_list = list(map(int, input().split()))

def prod_list(input_list: list) -> int:
    """squaring elements in a list
    doctests:
    >>> prod_list([1, 2, 3])
    6
    >>> prod_list([1, 4, 2, 10])
    80
    """
    product = reduce((lambda x, y: (x * y)), input_list)
    return product


# print(prod_list(input_list))
if __name__ == "__main__":
    import doctest
    doctest.testmod(name="prod_list", verbose=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
