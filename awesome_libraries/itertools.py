import itertools

# combine iterators
it = itertools.chain([1, 2, 3], [4, 5, 6])


# repeat a value
it = itertools.repeat("hello", 3)
print(list(it))


# repeat an iterator's items
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)


# split an iterator
it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))
print(list(it2))
print(list(it3))


# zip unequal length iterators with a default value
keys = ["one", "two", "three"]
values = [1, 2]
it = itertools.zip_longest(keys, values)
longest = list(it)
print(longest)


#
