
class Human:
    def __init__(self, name, age, height, gender):
        self.my_name = name
        self.age = age
        self.height = height
        self.gender = gender

    def __str__(self):
        return f"Name: {self.my_name}\n" \
               f"Age: {self.age}\n" \
               f"Height: {self.height}\n" \
               f"Gender: {self.gender}\n" \

    def can_calculate(self, number_1, number_2):
        summary = number_1 + number_2
        return summary
    def can_say_hello(self):
        return "Hello World"


class Programmer(Human):
    def __init__(self, name, age, height, gender, language, fast_typing, logic_thinking):
        super().__init__(name, age, height, gender)
        self.language = language
        self.fast_typing = fast_typing
        self.logic = logic_thinking

    def can_feely_use_laptop(self):
        print("Yep, I can felly use laptop like a God")

    def __str__(self):
        return f"Language {self.language}\n" \
               f"Fast_Typing {self.fast_typing}\n" \
               f"Logic {self.logic}\n" \

human_1 = Human(name = "Adilet", age=24, height=189, gender="male")
human_2 = Human("Aelin", 20, 179, "female")
print(human_1.can_calculate(int(input("First: ")), int(input("Second: "))))
print(human_2.can_say_hello())
print(human_1)
print(human_2)
proger = Programmer(language= "Python", fast_typing=True, logic_thinking=True, name="Adilet", age=24, height=189, gender="male")
print(proger)