class atm(object):

  def __init__(self, owner, cardNumber, pinNumber):
    self.owner=owner
    self.cardNumber=cardNumber
    self.pinNumber=pinNumber

  def CashWithdrawl(self):
    input=("Enter amount to withdraw:-")  
    print("withdrawing...")

  def BalanceEnquiry(self):
    print("Showing balance...")

card1 = atm("Sara", 231 , 543)

print(card1.CashWithdrawl())
