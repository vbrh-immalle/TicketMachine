import datetime
import hashlib

class TicketMachine:
    def __init__(self, cost):
        self.price = cost
        self.balance = 0
        self.total = 0

    def insertMoney(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Use a positive amount rather than: " + str(amount))

    def printTicket(self):
        if self.balance >= self.price:
            print("##################")
            print("# Ticket")
            print("# " + str(self.price) + " cents.")
            print("##################")
            print()
            self.total += 1
        else:
            shortage = self.price - self.balance
            print("You must insert at least: " + str(shortage) + " more cents.")

    def refundBalance(self):
        amountToRefund = self.balance
        self.balance = 0
        return amountToRefund
    
    def printAdminTicket(self, password, useHash=False):
        loggedIn = False

        print("~" * 40)
        print("~ Admin ticket ")
        print("~ " + str(datetime.datetime.now()))
        print("~")

        if useHash:
            print("~ Trying to login with hashed password...")
            algo = hashlib.sha1()
            algo.update(password.encode('utf-8'))
            pwdhash = algo.hexdigest()
            if pwdhash == 'f8b971d33bf56ffd1723a924d4a782a4370f4aa8':
                loggedIn = True
        else:
            print("~ Trying to login with cleartext password...")
            if password == 'marktaandeel':
                loggedIn = True

        if loggedIn:
            print("~ Total sales: " + str(self.total))
        else:
            print("~ Error: wrong password")

        print("~" * 40)

if __name__ == "__main__":
    t = TicketMachine(23)
    print(t.price)
    t.insertMoney(-3)
    t.insertMoney(14)
    t.printTicket()
    t.insertMoney(40)
    t.printTicket()
    t.printAdminTicket("woops")
    t.printAdminTicket("marktaandeel", True)
    t.printAdminTicket("marktaandeel")




