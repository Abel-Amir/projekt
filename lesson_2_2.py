class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.language = language
        self.soft = soft_skills
        self.laptop = laptop
        self.salary = salary

    def say_which_language(self):
        return f"Im using {self.language}"
    def __str__(self):
        return f"Language : {self.language}\n" \
               f"Soft-skills : {self.soft}\n" \
               f"Laptop : {self.laptop}\n" \
               f"Salary : {self.salary}"

junior_1 = Junior(language="Python",
                  soft_skills="Good Enought",
                  laptop="Gaming laptop",
                  salary="300$")

#print(junior_1)

class Middle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable):
        super().__init__(language, soft_skills, laptop, salary)
        self.fast_resolving = fast_resolving
        self.reliable = reliable

    def __str__(self):
        return super(Middle, self).__str__() + f"\nResolving : {self.fast_resolving}\n" \
                                               f"Reliable : {self.reliable}"

midle_1 = Middle(language="Python",
                 soft_skills="Good Enought",
                 laptop="Gaming laptop",
                 salary="3000$",
                 fast_resolving="Often",
                 reliable=True)
print(midle_1. say_which_language())
print(midle_1)

class Senior(Middle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable, arhitecture, leading_skill):
        super().__init__(language, soft_skills, laptop, salary, fast_resolving, reliable)
        self.arhitecture = arhitecture
        self.leading_skill = leading_skill

    def __str__(self):
        return super(Senior, self).__str__() + f"\nArhitecture : {self.arhitecture}\n" \
                                        f"Leading skill : {self.leading_skill}"


senior_1 = Senior(language="Python",
                soft_skills="Good Enought",
                laptop="Gaming laptop",
                salary="6000$",
                fast_resolving="Often",
                reliable=True,
                arhitecture=True,
                leading_skill=True)

print(senior_1)

