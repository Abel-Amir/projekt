class Summa:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def search_index(self):
        for index in range(len(self.numbers)):
            for internal_index in range(index + 1, len(self.numbers)):
                if (self.numbers[index] + self.numbers[internal_index]) == self.desired_sum:
                    return [index, internal_index]
        return None

    def __str__(self):
        return f'List of numbers: {self.numbers}\n' \
               f'Desired number: {self.desired_sum}\n'


selected_number = Summa(numbers=[3, 6, 1, 8, 10, 15, 4], desired_sum=10)
print(selected_number)
print(selected_number.search_index())