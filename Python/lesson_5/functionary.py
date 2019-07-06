def many(*arg, **kvargs):
    print(arg)
    print(kvargs)

many(1, 2, 3, x = "fifty six", y = "forty foor")