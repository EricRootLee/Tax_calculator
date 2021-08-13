class Person:
    def __init__(self, name: str, age: int, salary: int, net_pay: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.net_pay = net_pay

    def calc_tax(self, tax) -> int:
        income_tax = self.salary * (tax / 100)
        net_pay = self.salary - income_tax
        return net_pay

    def total_calc_tax(self) -> int:
        if 0 < self.age <= 45:
            return self.calc_tax(9)
        elif 46 <= self.age <= 65:
            return self.calc_tax(5)
        else:
            return self.calc_tax(3)
