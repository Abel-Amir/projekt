# Задание :
# 1. Создать зоопарк со своими условиями для животных
# 2. Создать классы объектов животных с их характерными чертами
# 3. Создать определенное количество объектов для каждого класса объектов
# Дополнительные указания к дз:
# 1. Создать класс объекта Zoo_show для представлений
# 2. Дополнительная функция к нему для определения стоимости билета , учитывая какое
# представление было выбрано

class Animals_from_Madagascar:
    def __init__(self, name, color, height, age, gender):
        self.name = name
        self.color = color
        self.height = height
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Цвет: {self.color}\n" \
               f"Рост: {self.height}\n" \
               f"Возраст: {self.age}\n" \
               f"Пол: {self.gender}\n"

class Zoo(Animals_from_Madagascar):
    def __init__(self, name, color, height, age, gender, tricks, country):
        super().__init__(name, color, height, age, gender)
        self.tricks = tricks
        self.country = country

    def __str__(self):
        return super().__str__()+f"\n" \
               f"Трюки {self.tricks}\n" \
               f"Страна {self.country}\n"

lion = Zoo (name="Alex", color="light brown",
            height= 1.6, age=10, gender="male", tricks= "acrobatics, growl", country= "Africa")
giraffe = Zoo (name="Melman", color="orange-brown",
            height= 6.3, age=12, gender="male", tricks= "walks the tightrope", country= "New York")
penguin = Zoo(name="Kowalski", color="black-white",
            height= 0.49, age=14, gender="male", tricks= "very smart", country= "Northern Russia")

class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0

        if(zoo.name == "Alex"):
            self.ticket = "30$"
        if (zoo.name == "Melman"):
            self.ticket = "40$"
        if (zoo.name == "Kowalski"):
            self.ticket = "20$"

    def tickete(self):
        return "The show will cost " + self.ticket

    def __str__(self):
        return f"{self.zoo.name} will show {self.zoo.tricks}"

show1 = Zoo_show(lion)
show2 = Zoo_show(giraffe)
show3 = Zoo_show(penguin)

print(show1)
print(show1.tickete())

print(show2)
print(show2.tickete())

print(show3)
print(show3.tickete())



