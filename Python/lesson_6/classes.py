class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.molt = 0
        print("Orange created") # визуализация создания обьекта

    def rot(self, day, temp):
        self.molt = day*temp

or_1 = Orange(10, "orange")
print(or_1)
print(or_1.weight)
print(or_1.color)
print(or_1.molt)

or_1.weight = 60
or_1.color = "dark"
print(or_1)
print(or_1.weight)
print(or_1.color)

or_1.rot(10, 18)
print(or_1.molt)