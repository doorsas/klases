class Indas:
    def __init__(self,name :str,capacity: int) -> None :
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return self.name + ' ' + str(self.capacity)

    def ipilti(self,kiekis: int):
        self.capacity += kiekis
        return self.capacity

    def ispilti(self,kiekis: int):
        self.capacity -= kiekis
        return self.capacity




asotis = Indas('Asotis', 50)
indas =  Indas('Indas', 20 )




print (asotis)
print (indas)
