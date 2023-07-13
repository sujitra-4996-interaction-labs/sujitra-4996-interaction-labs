class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, num):
        if num % 2 == 0:
            return (f"Factors of {num} is {num // 2} and {num // 2}")
        else:
            return (f"Factors of {num} is {num // 2} and {num // 2+1}")

    @staticmethod
    def is_valid_divisor(num):
        if num != 0:
            return f"{num} is a valid divisor"
        else:
            return f"{num} is not a valid divisor"


if __name__ == '__main__':
    numbers = Numbers(2, 3)
    print(f'2 + 3 is {numbers.add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))