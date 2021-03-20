class ATM(object):

    def __init__ (self, bank, savings_amount, card_no):
        self.bank = bank
        self.savings_amount = savings_amount
        self.card_no = card_no

    def sign_in(self):
        print("Signed In")

    def withdrawl(self):
        print("You have auto withdrawled $1")

    def card_no(self):
        print(self.card_no)

Om = ATM("ICICI", "2", "6758-1407-2964")

print(Om.sign_in())
print(Om.withdrawl())