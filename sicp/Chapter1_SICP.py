#!/usr/bin/env python

# In[3]:


def square(x):
    return mul(x, x)


from math import exp, sqrt
from operator import add, mul, sub

# In[13]:


def pressure(v, t, n):
    """Hoddie"""
    k = 1.38e-23  # boltzmann constant
    return n * k * t / v


pressure(1000, 100, 1.01)


# In[14]:


help(pressure)


# In[2]:


abs(-5676575)


# In[4]:


def absolute_value(x):
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


# In[6]:


absolute_value(-4)


# In[2]:


def fib(n):
    pred, curr = 0, 1
    k = 2
    while k < n:
        pred, curr = curr, curr + pred
        k = k + 1
    return curr


fib(3)


# [StackOverflow Link](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
# [Doctest Good Explaination](https://docs.python.org/3/library/doctest.html)
#
# ### Example "doctest", "main", "execution order"
# import time, thread
#
#
#     def myfunction(string, sleeptime, lock, *args):
#     while True:
#         lock.acquire()
#         time.sleep(sleeptime)
#         lock.release()
#         time.sleep(sleeptime)
#
#     if __name__ == "__main__":
#     lock = thread.allocate_lock()
#     thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
#     thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
#
#
#  When the Python interpreter reads a source file, it executes all of the code found in it.
#
# Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
#
# In the case of your script, let's assume that it's executing as the main function, e.g. you said something like
#
# python threading_example.py
# on the command line. After setting up the special variables, it will execute the import statement and load those modules. It will then evaluate the def block, creating a function object and creating a variable called myfunction that points to the function object. It will then read the if statement and see that __name__ does equal "__main__", so it will execute the block shown there.
#
# One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. Alternatively, it can also be imported and used in another module. By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
#
# See [this page](http://ibiblio.org/g2swap/byteofpython/read/module-name.html) for some extra details.
#

# In[26]:


def sum_naturals(n):
    """Return the sum of the first n natural numbers


    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


# In[27]:


from doctest import run_docstring_examples

run_docstring_examples(sum_naturals, globals())


# When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option.
#
#       python3 -m doctest <python_source_file>

# In[1]:


# General Method functions for Iterative improvement.
def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess


def near(x, f, g):
    return approx_eq(f(x), g(x))


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def successor(k):
    return k + 1


# In[4]:


# Golden Ratio using above GMF's.
def golden_update(guess):
    return 1 / guess + 1


def golden_test(guess):
    return near(guess, square, successor)


iter_improve(golden_update, golden_test)


# In[11]:


# Nested Functions, say you have an update function that requires two statements.
# Computing the square root of a number.


def average(x, y):
    return (x + y) / 2


def sqrt_update(guess, x):
    return average(guess, x / guess)


# Nested Function
def square_root(x):
    def update(guess):
        return average(guess, x / guess)

    def test(guess):
        return approx_eq(square(guess), x)

    return iter_improve(update, test)


square_root(81)


# In[14]:


# FxNs as returned values


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


add_one_square = compose1(square, successor)

add_one_square(12)


# In[15]:


def compose1(f, g):
    return lambda x: f(g(x))


# #### Newton-raphson
# Newton's method is a classic iterative approach to finding the arguments of a mathematical function that yield a return value of 0. These values are called roots of a single-argument mathematical function. Finding a root of a function is often equivalent to solving a related math problem.
#
# * The square root of 16 is the value x such that: square(x) - 16 = 0
#
# * The log base 2 of 32 (i.e., the exponent to which we would raise 2 to get 32) is the value x such that: pow(2, x) - 32 = 0
#
# Thus, a general method for finding roots will also provide us an algorithm to compute square roots and logarithms. Moreover, the equations for which we want to compute roots only contain simpler operations: multiplication and exponentiation.
#

# In[23]:


def square_root(a):
    return find_root(lambda x: square(x) - a)


def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)


# Newton update expresses the computational process of following
# the tangent line to zero. Approximate the derivate of the function by
# computing its slope over a very small interval.


def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta


def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)

    return update


def find_root(f, initial_guess=10):
    def test(x):
        return approx_eq(f(x), 0)

    return iter_improve(newton_update(f), test, initial_guess)


logarithm(100, 10)
print(logarithm)


# In[22]:


##Trace Functions


def trace1(fn):  # higher order fn defined
    def wrapped(x):
        print("->", fn, "(", x, ")")
        return fn(x)

    return wrapped


@trace1  # decorator, eq. to triple=trace1(triple)
def triple(x):
    return 3 * x


triple(12)


# [Memoization - Trace/Wrapper/Decorator Tutorial](http://programmingbits.pythonblogs.com/27_programmingbits/archive/50_function_decorators.html)
#
#

# In[24]:


# Memoization for fibonacci


def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Memoization function, no need to touch fib(n) function. Below function
# adds functionality to fib. Fib is an argument to memoize(),
def memoize(f):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return helper


# [list/dict/set SO](https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set/3489100#3489100)
# A `list` keeps order, `dict` and `set` don't: when you care about order, therefore, you must use `list` (if your choice of containers is limited to these three, of course;-).
#
# `dict` associates with each key a value, while `list` and `set` just contain values: very different use cases, obviously.
#
# `set` requires items to be hashable, `list` doesn't: if you have non-hashable items, therefore, you cannot use `set` and must instead use `list`.
#
# `set` forbids duplicates, `list` does not: also a crucial distinction.  (A "multiset", which maps duplicates into a different count for items present more than once, can be found in `collections.Counter` -- you could build one as a `dict`, if for some weird reason you couldn't import `collections`, or, in pre-2.7 Python as a `collections.defaultdict(int)`, using the items as keys and the associated value as the count).
#
# Checking for membership of a value in a `set` (or `dict`, for keys) is blazingly fast (taking about a constant, short time), while in a list it takes time proportional to the list's length in the average and worst cases.  So, if you have hashable items, don't care either way about order or duplicates, and want speedy membership checking, `set` is better than `list`.
#

# In[49]:


def iscap(s):
    return len(s) > 0 and s[0].isupper()


g = "University of California and Nevada Computer Sciences and Aritificial Intelligence Department"
h = list(filter(iscap, g.split()))


def first(s):
    return s[0]


def acronym(name):
    return tuple(map(first, filter(iscap, name.split())))


acronym(g)


# In[ ]:
