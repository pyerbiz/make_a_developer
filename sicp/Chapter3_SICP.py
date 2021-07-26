#!/usr/bin/env python

# In[3]:


def memo(f):
    """ Return a memoized version of  a single argument function f."""
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


# In[4]:


def count_change(a, kinds=(50, 25, 10, 5, 1)):
    """Return the number of ways to change amount A using coin kinds"""
    if a == 0:
        return 1
    if a < 0 or len(kinds) == 0:
        return 0
    d = kinds[0]
    return count_change(a, kinds[1:]) + count_change(a - d, kinds)


# In[5]:


count_change1 = memo(count_change)


# In[6]:


get_ipython().run_line_magic("timeit", "count_change(100)")


# In[7]:


get_ipython().run_line_magic("timeit", "count_change1(100)")


# In[9]:


count_change1(100)


# ### __logarithmic Growth__

# In[15]:


def square(x):
    return x * x


def fast_exp(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n // 2))
    return b * (fast_exp(b, n - 1))


# In[16]:


fast_exp(3, 100)


# In[13]:


import math

pow(3, 50)


# In[14]:


get_ipython().run_line_magic("timeit", "fast_exp (2,100)")


# In[17]:


a = [(1, 2, 3), (4, 5, 6)]


# In[1]:


help(dir)


# In[6]:


dir()


# In[13]:


count_change1.__closure__


# In[14]:


def initCounter():
    x = 0

    def counter():
        x += 1  ##Error, x not defined
        print(x)

    return counter


# count = initCounter()

# count()


# In[16]:


count = initCounter()
count()


# In[1]:


term = "Lizards and Amphibians not salamander or newt"
re.sub(r"\b(not|or|and)\b", lambda m: m.group().upper(), term)
"Lizards AND Amphibians NOT salamander OR newt"

re.sub(r"(\w+)(II+)(\w*)", replacement, "I am stiII here.")
import re

# In[23]:


def replacement(match):
    if match.group(1):
        return "-"
    if match.group(2):
        return ".jav"


mystr = "remote_execute___jenkin%.java"


# In[26]:


re.sub(r"(_{2,3})(\.java$)", replacement(match), mystr)


# In[ ]:


re.sub("_{2,3}", "_", re.sub(r"\.java$", ".jav", name))
name = re.sub("_{2,3}", "_", name)
name = re.sub(r"\.java$", ".jav", name)


# In[19]:


import re

name = "remote_execute___jenkin%.java"

fname = re.sub(r"(_{2,3})(\.java$)", my_repl, name)

fname


# In[20]:


class Rlist:
    """A recursive list consiting of the first element and the rest"""

    class EmptyList:
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.first is not Rlist.empty:
            args += ", {}".format(repr(self.rest))
        return f"Rlist ({args})"

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]


# In[21]:


s = Rlist(1, Rlist(2, Rlist(3)))
s.rest


# In[22]:


print(len(s))
print(s[1])


# In[30]:


def extend_rlist(s1, s2):
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))


type(extend_rlist(s.rest, s))


# In[31]:


def map_rlists(s, fn):
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlists(s.rest, fn))


# In[32]:


def ex_map(a):
    return a * a


# In[33]:


map_rlists(s, ex_map)


# In[34]:


def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)

    if fn(s.first):
        return Rlist(s.first, rest)
    return rest


# In[35]:


filter_rlist(s, lambda x: x % 2 == 1)


# In[36]:


help(repr)


# In[37]:


repr(tuple)


# In[38]:


type(tuple)


# In[39]:


type(str)


# In[57]:


class Tree:
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.right = right
        self.left = left

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += " ,  {}, {}".format(repr(self.left), repr(self.right))
        return f"Tree ({args})"


def fib_tree(n):

    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    return Tree(left.entry + right.entry, left, right)


# In[62]:


fib_tree(4)


# In[ ]:


dir(Tree)


# In[49]:


type(fib_tree(5))


# In[63]:


help(re.sub)


# In[64]:


"Joo" == "Joo"


# In[65]:


"Joo" == "Joo"


# In[108]:


m = [5, 6, 7]
n = [5, 6, 7]
m is n

p = " bar"
q = " bar"
p is q


# ## Amazing study on string comparison - is vs ==
#
# https://stackoverflow.com/questions/24245324/about-the-changing-id-of-an-immutable-string

# In[109]:


print(id(p), id(q))


# In[93]:


list_1 = ["foo", "has", 1, 2, [5, 6, 7], (9, 6), " bar", " baz"]
list_2 = ["foo", "has", 1, 2, [5, 6, 7], (9, 6), " bar", " baz"]


# In[ ]:


for f, b in zip(list_1, list_2):
    print(f is b)


# In[ ]:


for f, b in zip(list_1, list_2):
    print(f == b)


# In[ ]:
