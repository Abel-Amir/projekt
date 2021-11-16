class Wizzard:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def emailing(self):
        email = f"{self.first}, {self.last}@gmail.com"
        return email


    @property
    def fullname(self):
        name = self.first + "" + self.last
        return name

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
    def __str__(self):
        return f"Fullname : {self.first} {self.last}"

wiz= Wizzard(first="Liz", last="Prostokwashevna",
             email= "liz.Prostokwashevna@gmail.com")
print(wiz)
print(wiz.fullname())
print(wiz.emailing())
wiz.first = "Aelin"
print(wiz.fullname)