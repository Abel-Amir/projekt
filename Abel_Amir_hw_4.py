class TimeDesk:

    def convert(self, seconds, minutes, hours, days):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days

    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    seconds = int(input("Enter a number of seconds: "))

    days = (seconds // seconds_in_day)
    seconds = seconds - (days * seconds_in_day)

    hours = (seconds // seconds_in_hour)
    seconds = seconds - (hours * seconds_in_hour)

    minutes = (seconds // seconds_in_minute)
    seconds = seconds - (minutes * seconds_in_minute)

    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(days, hours, minutes, seconds))


class Car:

    def init(self, name, model, engine, year):
        self.name = name
        self.model = model
        self.engine = engine
        self.year = year

    @staticmethod
    def nickname(self):
        nickname = f"\"{self.name}\". {self.model}"
        return nickname

    @property
    def characteristics(self):
        properties = self.engine + " " + self.year
        return properties

    @characteristics.setter
    def characteristics(self, properties):
        self.engine, self.year = properties.split()

    @characteristics.deleter
    def characteristics(self):
        self.engine = None
        self.year = None

    def str(self):
        return f"Nickname: \"{self.name}\" {self.model}\n" \
               f"Characteristics: {self.engine}, {self.year} "


porsche = Car("Porsche", "Panamera", "3996см³", "2020")
print(porsche)