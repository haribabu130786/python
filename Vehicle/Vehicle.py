class Vehicle:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour


class TwoWheeler(Vehicle):
    def __init__(self, type, colour, company_name, reg_amt):
        super().__init__(type, colour)
        self.company_name = company_name
        self.reg_amt = reg_amt

    def display(self):
        print('{} {} {}'.format(super().__str__(), self.reg_amt, self.company_name))


class FourWheeler(Vehicle):
    def __init__(self, type, colour, company_name, reg_amt):
        super().__init__(type, colour)
        self.company_name = company_name
        self.reg_amt = reg_amt

    def display(self):
        print('{} {} {}'.format(super().__str__(), self.reg_amt, self.company_name))


res = FourWheeler(4, 'black', 'hero', 6000)
print(res.display())
rev= TwoWheeler(2,'white','honda',5000)
print(rev.display())