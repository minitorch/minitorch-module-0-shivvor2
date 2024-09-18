"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, TypeVar, Any

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    """Multiplies two numbers

    Args:
    ----
        x (float): Numerical input
        y (float): Numerical input

    Returns:
    -------
        float: Product of both x and y

    """
    return x * y


def id(x: float) -> float:
    """Returns the input unchanged"""
    return x


def add(x: float, y: float) -> float:
    """Adds two numbers

    Args:
    ----
        x (float): Numerical input
        y (float): Numerical input

    Returns:
    -------
        float: Sum of both x and y

    """
    return x + y


def neg(x: float) -> float:
    """Negates a number

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: the negation of the input

    """
    return -x


def lt(x: float, y: float) -> bool:
    """Checks if one number is less than another

    Args:
    ----
        x (float): Numeric input, Base Value to be compared
        y (float): Numeric input, additional number to be compared with

    Returns:
    -------
        bool: Whether x < y

    """
    return x < y

def eq(x: float, y: float) -> bool:
    """Checks if two numbers are equal

    Args:
    ----
        x (float): Numeric input
        y (float): Numeric input

    Returns:
    -------
        bool: Whether if x equals y

    """
    return x == y


def max(x: float, y: float) -> float:
    """Returns the larger of two numbers

    Args:
    ----
        x (float): Numeric input
        y (float): Numeric input

    Returns:
    -------
        float: The largest of x and y

    """
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    """Checks if two numbers are close in value

    Args:
    ----
        x (float): Numeric input
        y (float): Numeric input

    Returns:
    -------
        bool: True is difference between x and y < 0.01 (1e^-2)

    """
    return abs(x - y) < 0.01


def sigmoid(x: float) -> float:
    r"""Calculates the sigmoid function

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$

    """
    if x >= 0:
        result = 1 / (1 + math.exp(-x))
    else:  # x < 0
        result = math.exp(x) / (1 + math.exp(x))

    return result


def relu(x: float) -> float:
    """Applies the ReLU Activation function

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: Input after applying ReLU

    """
    return x - min(0, x)


def log(x: float) -> float:
    """Calculates the natural logarithm

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: input after applying logarithm

    """
    return log(x)


def exp(x: float) -> float:
    """Calculates the exponenatial function

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: Exponentialized input

    """
    return math.exp(x)


def inv(x: float) -> float:
    """Calculates the reciprocal

    Args:
    ----
        x (float): Numeric input

    Returns:
    -------
        float: Reciprocal (1/x) of the input (x)

    """
    return 1 / x


def log_back(x: float, y: float) -> float:
    """Computes the derivative of log times a second arg

    Args:
    ----
        x (float): First input, to be applied to the derivative of log
        y (float): Second numerical input to be multiplied to the result of the first input

    Returns:
    -------
        float: 1/x * y

    """
    return (1 / x) * y


def inv_back(x: float, y: float) -> float:
    """Computes the derivative of reciprocal times a second arg

    Args:
    ----
        x (float): First input, to be applied to the derivative of recipocal
        y (float): Second numerical input to be multiplied to the result of the first input

    Returns:
    -------
        float: -(1/x^2)*y

    """
    return -(1 / x**2) * y


def relu_back(x: float, y: float) -> float:
    """Computes the derivative of ReLU times a second arg

    Args:
    ----
        x (float): First input, to be applied to the derivative of ReLU
        y (float): Second numerical input to be multiplied to the result of the first input

    Returns:
    -------
        float: 1*y if x >= 0 else 0*y = 0

    """
    return y if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

# Core functions:
T_map = TypeVar("T_map")


def map(x: Iterable[T_map], func: Callable[[T_map], Any]) -> Iterable[Any]:
    """Higher-order function that applies a given function to each element of an iterable

    Args:
    ----
        x (Iterable[T]): Input Iterable of a certain type T
        func (Callable[[T], Any]): Mapping function

    Returns:
    -------
        Iterable[Any]: Input Iterable after applying the mapping function (as a list)

    """
    return [func(x_i) for x_i in x]


T_zipWith_x = TypeVar("T_zipWith_x")
T_zipWith_y = TypeVar("T_zipWith_y")


# Did not do length check
# Error caused by both iterables having different lengths should be handled by python itself
def zipWith(
    x: Iterable[T_zipWith_x],
    y: Iterable[T_zipWith_y],
    func: Callable[[T_zipWith_x, T_zipWith_y], Any],
) -> Iterable[Any]:
    """Higher-order function that combines elements from two iterables using a given function

    Args:
    ----
        x (Iterable[T_1]): Input Iterable of a certain type T_1
        y (Iterable[T_2]): Input Iterable of a certain type T_2
        func (Callable[[T_1, T_2], Any]): Function that takes in 2 inputs of type T_1, T_2 respectively and returns a result


    Returns:
    -------
        Iterable[Any]: Returned iterable by combining x and y with func

    """
    return [func(x_i, y_i) for x_i, y_i in zip(x, y)]


T_reduce = TypeVar("T_reduce")


# TODO: Implement "Conquer and divide" approach for sized iterables
def reduce(
    x: Iterable[T_reduce], func: Callable[[T_reduce, T_reduce], T_reduce]
) -> T_reduce:
    """Higher-order function that reduces an iterable to a single value using a given function

    Args:
    ----
        x (Iterable[T]): Input Iterable of a certain type T
        func (Callable[[T], Any]): _description_

    Returns:
    -------
        Any: reduced value created using the operator and the iterable

    """
    iterator = iter(x)
    try:
        result = next(iterator)
    except StopIteration:
        raise ValueError("Cannot reduce an empty iterable")
    for item in iterator:
        result = func(result, item)
    return result


def negList(x: Iterable[float]) -> Iterable[float]:
    """Negate all elements in a list using map

    Args:
    ----
        x (Iterable[float]): Input iterable

    Returns:
    -------
        Iterable[float]: Negated input iterable (we return a list here)

    """
    return map(x, neg)


def addLists(x: Iterable[float], y: Iterable[float]) -> Iterable[float]:
    """Add corresponding elements from two lists using zipWith

    Args:
    ----
        x (Iterable[float]): Numeric input iterable
        y (Iterable[float]): Numeric input iterable

    Returns:
    -------
        Iterable[float]: Sum of both Iterables

    """
    return zipWith(x, y, add)


def sum(x: Iterable[float]) -> float:
    """Sum all elements in a list using reduce

    Args:
    ----
        x (Iterable[float]): Numeric input iterable

    Returns:
    -------
        float: Sum of all elements in x

    """
    return reduce(x, add)


def prod(x: Iterable[float]) -> float:
    """Calculate the product of all elements in a list using reduce

    Args:
    ----
        x (Iterable[float]): Numeric input iterable

    Returns:
    -------
        float: Product of all elements in x

    """
    return reduce(x, mul)
