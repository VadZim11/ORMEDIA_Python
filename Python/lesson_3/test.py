str_1, str_2, str_3= "it is fist", "it is second", "it is memory"

print(str_1[0], str_1[-1])
print(str_2[0], str_2[len(str_2)-1])
print(str_3[0], str_3[-1])
print(str_1[::6])
print(str_2[0:3])
print(str_3[4:8])

a = (str_1[0:5])
print(a[1])

list_1 = [1, 2, 3, 4]
list_2 = [2, 3, 4]
print(list_1)
print(list_1 + list_2)

list_3 = [i*2 for i in "hello"]
print(list_3)

list_4 = [i*2 for i in list_1 + list_2 if i != 3]
print(list_4)