class Tarif:
    def __init__(self, number, name, summary,):
        self.number = number
        self.name= name
        self.summary = summary

    def call(self):
        return f"This number: {self.number}, can call but with restriction"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Number : {self.number}\n" \
               f"Summary : {self.summary}"
number_1 = Tarif(name="Adilet",
                 number="0774446852",summary="120")
# print(number_1)

class UnlCallTarif(Tarif):

    def unl_call(self):
        return f"This number {self.number}, can call but with restriction"

    def __str__(self):
        return super(UnlCallTarif, self).__str__()

number_2 = UnlCallTarif(name="Aelin",number= "0774567834",
                        summary="1500")
# print(number_2)

class UnlInternetTarif(Tarif):

    def unl_internet(self):
        return f"Your internet package is unlimited"

    def __str__(self):
        return super(UnlInternetTarif, self).__str__()

number_3 = UnlInternetTarif(name="Georg", number="0777-123-456",
                            summary="400")
# print(number_3)

class DiamondTarif(UnlInternetTarif, UnlCallTarif):
    def __str__(self):
        return super(DiamondTarif, self).__str__()
diamond = DiamondTarif(name="Alex", number= "0774-888-888",
                       summary=12000)

print(diamond.unl_call())
print(diamond.unl_internet())
print(diamond)