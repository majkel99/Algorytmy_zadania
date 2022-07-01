class Queue:
    tab = []
    tab_length=0
    tab_max=10
    def add_to_q(self,obj):
        if self.tab_length<self.tab_max:
           self.tab+=[obj]
           self.tab_length+=1
        else:
            print("Tablica jest pełna!")
        return
    def remove_from_q(self):
        try:
            wynik = self.tab[0]
            self.tab = self.tab[1:]
            self.tab_length -= 1
            return wynik
        except Exception as e:
            print("Tablica jest pusta!")


    def find_element(self,element):
        try:
            return self.tab[element]
        except Exception as e:
            return e


test=Queue()
test.remove_from_q()
test.add_to_q(12)
test.add_to_q(76)
test.add_to_q(65)
print(test.remove_from_q())
print(test.tab)
print(test.find_element(2))
