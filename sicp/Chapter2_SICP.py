#!/usr/bin/env python

# In[11]:


# OBJECTS AS A METAPHOR

from datetime import date

today = date(2011, 9, 2)
str(date(2011, 12, 2) - today)
today.year
today.strftime("%A, %B %d")
# Objects, class, instances ofclass, attributes,
# methods (function valued attributes),behaviour and information.
# Dot notation-combined expression in Python


# In[12]:


# NATIVE DATA TYPES

type(today)

# Native data type properties, literals, native numeric types,float vs int


# In[15]:


# DATA ABSTRACTION

# compund structure, compound data value, lat long regarded as single
# conceptual unit,technique of isolating how data is represented vs how
# data is maniplated, assupmtions about data should be minimum
# Selectors and Constructors, finite binary expansion, # wishful thinking

"""make_rat(n, d) returns the rational number with numerator n and denominator d. #constructor
numer(x) returns the numerator of the rational number x. #selector
denom(x) returns the denominator of the rational number x.  #selector"""


def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + ny * dx, dx * dy)


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def eq_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


# we have defined operations on rational numbers defined, in terms of numer and
# denom and the constructor fxn make_rat. Need to glue together num & denom.


# In[18]:


# Tuples - a compound structure

pair = (1, 2)
x, y = pair
x
y
pair[0]
pair[1]

# indexing from 0 because we want to see how far is an element from the
# beginning of the tuple

from operator import getitem

getitem(pair, 0)


# In[19]:


def make_rat(n, d):
    return (n, d)


def numer(x):
    return getitem(x, 0)


def denom(x):
    return getitem(x, 1)


def str_rat(x):
    return "{}/{}".format(numer(x), denom(x))


# In[21]:


half = make_rat(1, 2)
str_rat(half)


# In[22]:


third = make_rat(1, 3)
str_rat(third)


# In[24]:


str_rat(mul_rat(half, third))


# In[25]:


str_rat(add_rat(third, third))


# In[29]:


# final evaluation above shows our implementation does not reduce rational numbers.
# need a function to compute greatest common denominator of integers

from fractions import gcd
from math import gcd


def make_rat(n, d):
    g = gcd(n, d)
    return (n // g, d // g)


# "//" expresses integer division , rounds down to fractional part of result of division.

str_rat(add_rat(third, third))


# In[55]:


# DIVE INTO PYTHON (FURTHER READING)
uid = "sa"
pwd = "secret"
print(pwd, "is not a passowrd for", uid)

usercount = (6,)
print("Users connected: %s" % (usercount))


# In[74]:


def make_pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y

    return dispatch


def getitem_pair(p, i):
    return p(i)


p = make_pair(3, 7)
getitem_pair(p, 1)


# In[77]:


k = (1, (2, (3, (4, None))))
type(k)


# In[4]:


empty_rlist = None


def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return (first, rest)


def first(s):
    """Return the first element of a recursive list s."""
    return s[0]


def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


# In[5]:


counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))
counts


# In[6]:


def len_rlist(s):
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


# In[16]:


getitem_rlist(counts, 3)


# In[25]:


def count(s, value):
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


digits = (2, 5, 6, 7, 7, 8, 9, 9, 0, 9, 2, 1, 3, 4)
count(digits, 9)


# In[29]:


def count(s, value):
    total = 0
    for j in s:  # s is iterable
        if j == value:
            total = total + 1
    return total


count(digits, 7)


# In[42]:


# sequence unpacking, rememember x,y=2,2 works. Similar syntax in For:

mypairs = ((2, 1), (2, 2), (6, 7), (8, 8), (3, 4))

# Count number of same value pairs


def countsame(s):
    total = 0
    for x, y in s:
        if x == y:
            total = total + 1
    return total


countsame(mypairs)


# In[46]:


tuple(range(1, 10))


# In[69]:


# LISTS

chinese_suits = ["coin", "string", "myriad"]
suits = chinese_suits
alphasuits = suits
betasuits = alphasuits

suits.pop()
suits.remove("string")
suits.append("cup")
suits.extend(("sword", "club"))
suits[2] = "spade"
suits[0:2] = ("heart", "diamond")
nest = list(suits)
nest[0] = suits

suits.insert(2, "joker")
nest


# In[72]:


# nest[0].pop(2)
suits


# In[66]:


suits is nest[0]


# In[78]:


suits is [
    "heart",
    "diamond",
    "spade",
    "club",
]  # because suits is a list object not just
# its values, which are compared here [....]


# In[76]:


suits is suits


# In[77]:


suits == nest[0]


# In[79]:


suits == ["heart", "diamond", "spade", "club"]


# In[87]:


# LIST IMPLEMENTATION WITH RECRUSIVE PROGRAMMING. ACTUAL IMPLEMENTATION IS HIDDEN IN PYTHON

# empty list, unique list
empty_rlist = None


# In[89]:


# first & rest concept of a sequene
def make_rlist(first, rest):
    return (first, rest)


def first(s):
    return s[0]


def rest(s):
    return s[1]


# In[92]:


# now to make a list, use nested function:
counts = make_rlist(
    1,
    make_rlist(
        2, make_rlist(7, make_rlist(5, make_rlist(8, make_rlist(12, empty_rlist))))
    ),
)
counts


# In[97]:


def len_rlist(s):
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


getitem_rlist(counts, 2)


# In[120]:


# len,getitem,pushfirst,popfirst,string,a convenience fxn


def make_mutable_rlist():
    contents = empty_rlist

    def dispatch(message, value=None):
        nonlocal contents
        if message == "length":
            return len_rlist(contents)
        elif message == "getitem":
            return getitem_rlist(contents, value)
        elif message == "push_first":
            contents = make_rlist(value, contents)
        elif message == "pop_first":
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == "str":
            return str(contents)

    return dispatch


# CONVENIENCE FUNCTION / ADDING ELEMENTS THE LIST


def to_mutable_rlist(source):
    s = make_mutable_rlist()
    for element in reversed(source):
        s("push_first", element)
    return s


# In[122]:


s = to_mutable_rlist(counts)
type(s)


# In[125]:


s("length")


# In[126]:


len_rlist(counts)


# In[130]:


mylist = ["google", "amazon", "microsoft", "apple", "netflix"]

mys = to_mutable_rlist(mylist)
type(mys)


# In[132]:


mys("length")


# In[146]:


counts = make_rlist(
    1,
    make_rlist(
        2, make_rlist(7, make_rlist(5, make_rlist(8, make_rlist(12, empty_rlist))))
    ),
)
len(counts)
len_rlist(counts)
s("length")
suits = ["heart", "diamond", "spade", "club"]


# In[149]:


# MYISSUE

counts = make_rlist(
    1,
    make_rlist(
        2, make_rlist(7, make_rlist(5, make_rlist(8, make_rlist(12, empty_rlist))))
    ),
)
counts
# inbuilt function sees the comma outside the inner brackets hence counts only 2
len(counts)

# this function doesn't stop counting till it reached the 'empt_rlist' value at the end of the list, hence counts recursively = 6
def len_rlist(s):
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


len_rlist(counts)

# built a message based function that calculates length based on 'len_rlist' and fit it into below program:


def make_mutable_rlist():
    contents = empty_rlist

    def dispatch(message, value=None):
        nonlocal contents
        if message == "length":
            return len_rlist(contents)
        elif message == "getitem":
            return getitem_rlist(contents, value)
        elif message == "push_first":
            contents = make_rlist(value, contents)
        elif message == "pop_first":
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == "str":
            return str(contents)

    return dispatch


# to use this program used below function


def to_mutable_rlist(source):
    s = make_mutable_rlist()
    for element in reversed(source):
        s("push_first", element)
    return s


s = to_mutable_rlist(suits)

# new function s=... should give us the length based on 'length message using len_rlist function

s("str")
s("length")


# <font color = green>__My issue__</font> was that I was getting different results for **len** and **len_rlist** for the same list. But this was happening when I was using the message function to fetch the length of the list, which uses **len_rlist**. When I was using **len_rlist** directly on the list, it was giving me the correct result. What I didn't realize, I was appling **to_mutable_rlist** to use the message fxn **len_rlist** on a list, that was already a mutable recursive list, made by  *counts=make_rlist(...(..))))*. Using **to_mutable_rlist** on this rlist gave me a new recursive list, which had the length 2.

# In[152]:


# Dictionaries
# getitem, setitem, # dispatch - keys and values


def make_dict():
    records = []

    # v is stored according to k , hence, if k=key return (remember wishful thinking). Iterable value here is records which is called (k,v) a pair.
    # hence return v will return corresponding value.

    def getitem(key):
        for k, v in records:
            if k == key:
                return v

    # setitem will take key, value and attach new value to the key, wether or not key already exists.

    def setitem(key, value):
        for item in records:
            if item[0] == key:
                item[1] = value
                return
        records.append([key, value])

    def dispatch(message, key=None, value=None):
        if message == "getitem":
            return getitem(key)
        elif message == "setitem":
            return setitem(key, value)
        elif message == "keys":
            return tuple(k for k, _ in records)
        elif message == "values":
            return tuple(v for _, v in records)
        elif message == "string":
            return str(records)

    return dispatch


# In[160]:


mydict = make_dict()
mydict("setitem", 3, 4)
mydict("setitem", ("angel", "misha", "CMD"), ("42", "Rstudio", "Bash"))
mydict("string")


# ### Propogating constraints, Example
#
# <font color = blue>__Keywords:__</font> Constraints, Connectors, nonlocal, dictionaries, general linear method, association, dispatch

# In[ ]:


from operator import add, mul, sub, truediv


def inform_all_except(source, message, constraints):
    """Inform all constraints of the message except source"""
    for c in constraints:
        if c != source:
            c[message]()


def make_ternary_constraints(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a"""

    def new_value():
        av, bv, cv = [connector["has_val"]() for connector in (a, b, c)]
        if av and bv:
            c["set_val"](constraint, ab(a["val"], b["val"]))
        elif av and cv:
            b["set_val"](constraint, ac(a["val"], c["val"]))
        elif cv and bv:
            a["set_val"](constraint, cb(c["val"], b["val"]))

    def forget_value():
        for connector in (a, b, c):
            connector["forget"](constraint)

    constraint = {"new_val": new_value, "forget": forget_value}
    for connector in (a, b, c):
        connector["connect"](constraint)
    return constraint


def adder(a, b, c):
    """the constraint that a+b=c"""
    return make_ternary_constraints(a, b, c, add, sub, sub)


def multiplier(a, b, c):
    """the constraint that a*b=c"""
    return make_ternary_constraints(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """the constraint that connector=value"""
    constraint = {}
    connector["set_val"](constraint, value)
    return constraint


def make_connector(name=None):
    """A connector between constraints"""
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector["val"]
        if val is None:
            informant, connector["val"] = source, value
            if name is not None:
                print(name, "=", value)
            inform_all_except(source, "new_val", constraints)
        elif val != value:
            print("Contradiction detected", val, "vs", value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector["val"] = None, None
            if name is not None:
                print(name, "is forgotten")
            inform_all_except(source, "forget", constraints)

    connector = {
        "val": None,
        "set_val": set_value,
        "forget": forget_value,
        "has_val": lambda: connector["val"] is not None,
        "connect": lambda source: constraints.append(source),
    }
    return connector


celsius = make_connector("Celsius")
fahrenheit = make_connector("Fahrenheit")


def make_converter(c, f):
    """connect c to f with constraints from celsius to fahrenheit"""

    u, v, w, x, y = [make_connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


make_converter(celsius, fahrenheit)


# ## Implementing Classes and Objects
#
#

# In[2]:


def make_instance(cls):
    """return a new object instance, which is a dispatch dictionary"""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls["get"](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {"get": get_value, "set": set_value}
    return instance


# In[3]:


def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise"""
    if callable(value):

        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value


# In[4]:


def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary."""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class["get"](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    cls = {"get": get_value, "set": set_value, "new": new}
    return cls


# In[5]:


def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args"""
    instance = make_instance(cls)
    init = cls["get"]("__init__")
    if init:
        init(instance, *args)
    return instance


# In[6]:


def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""

    def __init__(self, account_holder):
        self["set"]("holder", account_holder)
        self["set"]("balance", 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self["get"]("balance") + amount
        self["set"]("balance", new_balance)
        return self["get"]("balance")

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self["get"]("balance")
        if amount > balance:
            return "Insufficient funds"
        self["set"]("balance", balance - amount)
        return self["get"]("balance")

    return make_class(
        {
            "__init__": __init__,
            "deposit": deposit,
            "withdraw": withdraw,
            "interest": 0.02,
        }
    )


# In[9]:


def init_instance1(cls, *args):
    """Return a new object with type cls, initialized with args"""
    instance = make_instance(cls)
    init = cls["get"]("__init__")
    # if init:
    # init (instance, *args)
    return init


# In[ ]:


# In[10]:


jim_acct = Account["new"]("Jim")
type(jim_acct)


# In[12]:


jim_acct["get"]("holder")


# In[13]:


jim_acct["get"]("interest")


# In[15]:


jim_acct["get"]("deposit")(20)


# In[16]:


jim_acct["get"]("withdraw")(5)


# In[20]:


jim_acct["set"]("interest", 0.04)
Account["get"]("interest")


# In[21]:


jim_acct["get"]("interest")


# ### Inheritance

# In[22]:


def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""

    def withdraw(self, amount):
        return Account["get"]("withdraw")(self, amount + 1)

    return make_class({"withdraw": withdraw, "interest": 0.01}, Account)


# In[23]:


CheckingAcc = make_checking_account_class()
jack_acct = CheckingAcc["new"]("jack")


# In[24]:


print(jack_acct["get"]("interest"))
print(jack_acct["get"]("deposit")(20))
print(jack_acct["get"]("withdraw")(9))


# ### Generic Operations
#
# Combining and manipulating objects of different types to build a large program. Till now we have used message functions, with dot expressions was what we have used till now.
#
# Using message passing, we endowed our abstract data types with behaviour directly. Using the object methaphor, we bundled together the representation of data and the methods used to manipulate that data to modularize data-driven programs with local state.
#

# In[1]:


def hexid(obj):
    return hex(id(obj))


def make_instance(cls):  # good with this
    """ Return a new object instance, which is a dispatch dictionary """

    def get_value(name):
        print("INSTANCE GET_VALUE", name, "from", hexid(attributes))
        if name in attributes:
            return attributes[name]
        else:
            value = cls["get"](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {"test": "Default Test"}
    print("Created instance attributes", hexid(attributes))
    instance = {"get": get_value, "set": set_value}
    return instance


def bind_method(value, instance):  # good with this
    """ Return a bound method if value is callable, or value otherwise """
    if callable(value):

        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value


def make_class(attributes, base_class=None):
    """ Return a new class, which is a dispatch dictionary. """

    def get_value(name):
        print("\nCLASS GET_VALUE", name, "from", hexid(attributes))
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class["get"](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    print("Creating class with attributes", hexid(attributes))
    cls = {"get": get_value, "set": set_value, "new": new}
    return cls


def init_instance(cls, *args):  # problem here
    """ Return a new object with type cls, initialized with args """
    instance = make_instance(cls)
    init = cls["get"]("__init__")
    if init:
        print("Calling init of", hexid(cls), "on", hexid(instance), "with", args)
        init(instance, *args)  # No return here
    return instance


def make_my_class():  # define a custom class
    # Create a simple __init__ for the class
    def __init__(inst, *args):
        print("INIT", hexid(inst), args)
        inst["set"]("data", args)

    # return a dict that implements class
    return make_class({"__init__": __init__})


# test

# create a class
my_class = make_my_class()

# create some class instances
jim = my_class["new"]("Jim")
jim["set"]("test", "Hello")

fred = my_class["new"]("Fred")

print("CLASS", hexid(my_class))
print("\nINSTANCE", hexid(jim))
print(jim["get"]("data"))
print(jim["get"]("test"))

print("\nINSTANCE", hexid(fred))
print(fred["get"]("data"))
print(fred["get"]("test"))


# In[3]:


help(hex)


# # Super SO References
#
# https://stackoverflow.com/questions/50769327/class-instance-implementation-initializing-instance-from-sicp-python/50871026#50871026
#
#
# https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures/20898085#20898085
#
#
# https://stackoverflow.com/questions/12919278/how-to-define-free-variable-in-python

# In[ ]:
