class payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"
    def reset(self):
        self.payment = "no"
        self.payment = int(input("insert new amount: "))
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount) +"$"
        else:
            return self.name + " is not paid yet"
        
nathan = payslips("Nathan", "no", 1000)
roger = payslips("Roger", "no", 2000)
print("{}\n{}".format(nathan.status(),roger.status()))
nathan.pay()
print("{}\n{}".format(nathan.status(),roger.status()))
nathan.reset()
print("{}\n{}".format(nathan.status(),roger.status()))
print(nathan.payment)