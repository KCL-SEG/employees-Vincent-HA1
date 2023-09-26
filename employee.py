"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, rate, hours=1):
        self.name = name
        self.pay = rate * hours
        self.description = f'{self.name} works on a'
        if hours>1:
            self.description+= f' contract of {hours} hours at {rate}/hour'
        else:
            self.description+= f' monthly salary of {rate}'

    def add_contract_commission(self, rate, noOfContracts):
        self.pay += rate * noOfContracts
        self.description+= f' and receives a commission for {noOfContracts} contract(s) at {rate}/contract'

    def add_bonus_commission(self, bonusAmount):
        self.pay += bonusAmount
        self.description+= f' and receives a bonus commission of {bonusAmount}'

    def get_pay(self):
        return self.pay

    def __str__(self):
        print(self.description + f'.  Their total pay is {self.pay}.')
        return self.description + f'.  Their total pay is {self.pay}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000)
renee.add_contract_commission(200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150)
jan.add_contract_commission(220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000)
robbie.add_bonus_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120)
ariel.add_bonus_commission(600)
