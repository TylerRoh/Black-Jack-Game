'''
This is going to be my module to track the money that the player has left
I think I will add the betting function in here maybe...
'''

class Account:

    def __init__(self,player,balance):

        self.player = player
        self.balance = balance

    def __str__(self):
        return f"{self.player}'s remaining balace is {self.balance}"

    def win(self,amount):
        self.balance += amount


    def bet(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f'You do not have enough funds for this bet, your remaining balance is {self.balance}')

#As far as I can tell, this one is finished all it does is keep track of the players balance.

if __name__ == '__main__':
    print('main')