import random

class Toyta:
    def __init__(self, name, wheel, seat, headlights, mirror):
        self.name = name
        self.wheel = wheel
        self.seat = seat
        self.headlights = headlights
        self.mirror = mirror

    def fuel(self):
        return f"This car : {self.name}, can drive but on diesel"

    def product(self):
        return f"In December 1997 production of {self.name} began in Japan"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Wheel : {self.wheel}\n" \
               f"Seat : {self.seat}\n" \
               f"Headlights : {self.headlights}\n" \
               f"Mirror : {self.mirror}\n"


toyta_1 = Toyta(name="Toyta Prius 1",
                wheel="winter",
                seat="leather",
                headlights=True,
                mirror=True)


# print(toyta_1)

class Toyta_prius_2(Toyta):
    def toyataprius2(self):
        return f"This car : {self.name}, can drive but on gasoline 92"

    def door(self):
        return f"{self.name} had a five-door hatchback type body"

    def __str__(self):
        return super(Toyta_prius_2, self).__str__()


toyta_2 = Toyta_prius_2(name="Toyta prius 2",
                        wheel="winter",
                        seat="leather",
                        headlights=True,
                        mirror=True)


# print(toyta_2)

class Toyta_prius_3(Toyta):
    def toyataprius3(self):
        return f"This car :{self.name}, can drive but on electricity"

    def powertrain(self):
        return f"{self.name} hybrid powertrain was 90% newer than the 2nd generation"

    def __str__(self):
        return super(Toyta_prius_3, self).__str__()


toyta_3 = Toyta_prius_3(name="Tayta prius 3",
                        wheel="summer",
                        seat="leather",
                        headlights=True,
                        mirror=True)


# print(toyta_3)

class Toyta_prius_hibrid(Toyta_prius_2, Toyta_prius_3):
    def __str__(self):
        return super(Toyta_prius_hibrid, self).__str__()


hibrid = Toyta_prius_hibrid(name="Toyta prius hibrid",
                            wheel="all seasinol",
                            seat="leather",
                            headlights=True,
                            mirror=True)
print(hibrid.toyataprius2())
print(hibrid.toyataprius3())
print(hibrid)


# Задание № 2 Множественное Наследование ( Один ко многим )
# 1. Создать 4 класса , один из них является супер-классом , от которого
# наследуются все остальные 3 класса
# 2. У супер класса должно быть как минимум 4 атрибута ( def __init__(self, atribut,
# atribut2): )
# 3. У каждого класса должно быть как минимум 2 метода ( def method(self): )
# 4. Также должны быть соблюдены def __str__(self) + super()
# 5. К каждому классу создать по одному объекту ( в итоге должно быть 4
# объекта )

class Sensei:
    def __init__(self, name, weight, height, name_sport):
        self.name = name
        self.weight = weight
        self.height = height
        self.name_sport = name_sport

    def bc(self):
        return f"{self.name_sport} appeared in 221 BC"

    def world(self):
        return f"{self.name} is world champion"

    def __str__(self):
        return f"Name : {self.name}\n" \
               f"Weight : {self.weight}\n" \
               f"Height : {self.height}\n" \
               f"Name Sport: {self.name_sport}"


sensei = Sensei(name="Brain",
                weight=53,
                height=170,
                name_sport="Kung-Fu")
print(sensei.bc())
print(sensei.world())
print(sensei)


class Apprentice(Sensei):
    def __init__(self, name, weight, height, name_sport, language, force):
        super().__init__(name, weight, height, name_sport)
        self.language = language
        self.force = force

    def acrobatic(self):
        return f"{self.name} is good at acrobatic moves"

    def trainer(self):
        return f"{self.name} received the title of Honored Trainer"

    def __str__(self):
        return super(Apprentice, self).__str__() + f"\n" \
                                                   f"Language : {self.language}\n" \
                                                   f"Force : {self.force}\n"


apprentice = Apprentice(name="Arlen",
                        weight=34,
                        height=175,
                        name_sport="Judo",
                        language="China, English",
                        force=True)
print(apprentice.acrobatic())
print(apprentice.trainer())
print(apprentice)


class Apprentice_2(Sensei):
    def __init__(self, name, weight, height, name_sport, dexterous, flexible):
        super().__init__(name, weight, height, name_sport)
        self.dexterous = dexterous
        self.flexible = flexible

    def soiable(self):
        return f"{self.name} is very sociable"

    def provide(self):
        return f"{self.name} can provide first aid"

    def __str__(self):
        return super(Apprentice_2, self).__str__() + f"\n" \
                                                     f"Dexterous : {self.dexterous}\n" \
                                                     f"Flexible : {self.flexible}\n"


apprentice_2 = Apprentice_2(name="Chingyz",
                            weight=32,
                            height=185,
                            name_sport="Taekwondo WTF",
                            dexterous=True,
                            flexible=True)
print(apprentice_2.soiable())
print(apprentice_2.provide())
print(apprentice_2)


class Apprentice_3(Sensei):
    def __init__(self, name, weight, height, name_sport, clever, kind):
        super().__init__(name, weight, height, name_sport)
        self.clever = clever
        self.kind = kind

    def trains(self):
        return f"{self.name} trains children"

    def children(self):
        return f"{self.name} knows how to find language with children"

    def __str__(self):
        return super(Apprentice_3, self).__str__() + f"\n" \
                                                     f"Clever : {self.clever}\n" \
                                                     f"Kind : {self.kind}\n"
apprentice_3 = Apprentice_3(name="Buble",
                            weight=33,
                            height=170,
                            name_sport="Athletics",
                            clever=True,
                            kind=True)
print(apprentice_3.trains())
print(apprentice_3.children())
print(apprentice_3)

# Задание № 3 Магические методы
# 1. Создать 2 класса с магическими методами
# 2. 1-ый класс это класс Кинотеатр , в котором будут фильмы и нужно использовать как минимум 2 магических метода для выведения фильма
# 3. Должен быть выбор фильмов и цена у каждого разный


class Cinema:
    def __init__(self, cinimas_name, geolocation_cinema, *films):
        self.cinema = cinimas_name
        self.geo = geolocation_cinema
        self.films = []
        for i in films:
            self.films.append(i)

    def __add__(self, film):
        self.films.append(film)
        print("Фильм добавлен")
        return self

    def show_film(self, film):
        ticket = random.randint(1, 6) * 50
        if(self.films.__contains__(film)):
            print(f"Фильм: {film}, Цена на билет: {ticket}")
        else:
            print("Такого фильма нет в прокате")

    def __sub__(self, film):
        try:
            self.films.remove(film)
            print("Фильм убран с проката")
        except:
            print("Фильма и так нет в прокате")
        return self

    def __str__(self):
        return f"Cinimas nam : {self.cinema}\n" \
               f"Geolocation cinema : {self.geo}\n" \
               f"Films {self.films}\n"



cosmopark = Cinema("Космопарк", "4 микрорайон")
cosmopark.show_film("Дюна")
cosmopark.show_film("Веном")
cosmopark = cosmopark + "Веном"
cosmopark = cosmopark + "Вечные"

cosmopark.show_film("Веном")
cosmopark.show_film("Вечные")
cosmopark = cosmopark - 'Веном'
cosmopark.show_film("Веном")

# 4. 2-ой класс это класс Старбакс в котором пишут имена на кофе
# 5. Если имя больше 9 символов пишут только 5 символов имени
# 6. Если имя меньше 5 пишут все символы имени
# 7. Использовать именно магические методы
class Starbucks:
    def __init__(self, name, geolocation, opening_year, manager):
        self.name = name
        self.geo = geolocation
        self.open = opening_year
        self.manager = manager
        self.costumers_names = []
    def __add__(self,customer):
        self.costumers_names.append(customer)
        return self
    def showCoffieName (self, name):
        if len (name) >= 5 :
            print(name[:5])
        else:
            print(name)

    def __str__(self):
        return f"Name : {self.name}\n" \
               f"Geolocetion : {self.geo}\n" \
               f"Opening Year : {self.open}\n" \
               f"Manager : {self.manager}\n"
starbucks_1 = Starbucks("Starbucks", "st. Chui 155", "6 may, 2018 year", "Advard")
print(starbucks_1)
print(starbucks_1.showCoffieName("Mihail"))
print(starbucks_1.showCoffieName("Bambilbi"))