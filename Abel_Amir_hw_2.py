# Задача №1 Наследование
# 1. Создать трехступенчатую концепцию (дед-отец-ребенок) любого примера который вам ближе
# 2. Все три класса должны иметь свои особенные методы и атрибуты как минимум два доп метода у каждого класса
# 3. Также создать хотя бы по одному объекту к каждому классу
class Family:
    def __init__(self, name, hair_color, height, weight, language):
        self.name = name
        self.hair_color = hair_color
        self.height = height
        self.weight = weight
        self.language = language

    def __str__(self):
        return f"Name : {self.name}\n" \
               f'Hair color : {self.hair_color}\n' \
               f'Height : {self.height}\n' \
               f"Weight : {self.weight}\n" \
               f'Language: {self.language}\n'

danil = Family(name= "Danil",
                      hair_color="white",
                      height=167,
                      weight=57,
                      language="Russia and Kyrgyz")
print(danil)

class Father(Family):
    def __init__(self, name, hair_color, height, weight, language, work, pension):
        super().__init__(name, hair_color, height, weight, language)
        self.work = work
        self.pension = pension

    def __str__(self):
        return super(). __str__() + f"" \
               f"Work : {self.work}\n" \
               f"Pension : {self.pension}\n"

class Son(Father):
    def __init__(self, name, hair_color, height, weight, language, work, pension, study, grade):
        super().__init__(name, hair_color, height, weight, language, work, pension)
        self.study = study
        self.grade = grade

    def __str__(self):
        return super().__str__() + f"" \
               f"Study : {self.study}\n" \
               f"Grade : {self.grade}\n"

kuba = Father(name= "Kubanichbek", hair_color= "Black",
              height=178, weight=34,
              language="Russian and English",
              work="Manager",
              pension=False)

mirbek = Son(name= "Mirbek", hair_color= " Brown",
             height=158, weight=14,
             language= "Kyrgyz and Russian",
             work=False,
             pension=False,
             study=True,
             grade=5)

print(kuba)
print(mirbek)

# Задача №2 Инкапсуляция
# 1. Создать один класс в котором вы пропишете по одному методу (внутреннего и защищенного)
# 2. В этом классе должно быть также по одному атрибуту (внутреннего и защищенного)
class Home:
    def __init__(self, color, room, members, heating):
        self.color = color
        self.room = room
        self._members = members
        self.__heating = heating
    def __show_heating(self):
        show = f"Show heating {self.__heating}"
        return show

    def _show_he_number_of_people(self):
        show = f"Show he number of people {self._members}"
        return show

    def __str__(self):
        return f"Color: {self.color}\n" \
               f"Room: {self.room}\n" \
               f"Members: {self._members}\n" \
               f"Heating : {self.__heating}\n"

home_1 = Home(color= "black amd white",
              room= 3,
              members= 4,
              heating= True)
print(home_1)

# Задача № 3 Полиморфизм без наследования
# 1. Создать три разных класса в котором будут одинаковые методы по названию например (attack)
# 2. Но логика этого самого метода будут разные как в случае примера с мечником , лучником и волшебником

class Mag:
    def attack(self):
        print("Колдует")

class Knight:
    def attack(self):
        print("Размахивать мечом")

class Goblin:
    def attack(self):
        print("Воровать")

mag_1 = Mag()
knight_1 = Knight()
goblin_1 = Goblin()
print(mag_1.attack())
print(knight_1.attack())
print(goblin_1.attack())

# Задача № 4 Полиморфизм с наследованием
# 1. Все тоже самое как в случае с Полиморфизмом без наследование , единственное различие здесь присутствует наследование
# трехступенчатой концепций (дед-отец-ребенок)

class Grand_father:
    def doing(self):
        print("Sleep")

class Dad(Grand_father):
    def doing(self):
        print("Working")

class Son(Dad):
    def doing(self):
        print("Studing")

grand_father_vasya = Grand_father()
dad_dima = Dad()
son_ulan = Son()

print(grand_father_vasya.doing())
print(dad_dima.doing())
print(son_ulan.doing())