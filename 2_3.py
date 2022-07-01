class Stack:
    tab=[]
    tab_length=0
    tab_max=5
    def add_to_stack(self,obj):
        if self.tab_length<self.tab_max:
            self.tab+=[obj]
            self.tab_length+=1
        else:
            print("Tablica jest pełna!")
    def remove_from_stack(self):
        try:
            wynik=self.tab[-1]
            self.tab=self.tab[:-1]
            self.tab_length -= 1
            return wynik
        except Exception as e:
            print("tablica jest pusta!")
    def find_element(self, element):
        try:
            return self.tab[element]
        except Exception as e:
            return e

test=Stack()
test.remove_from_stack()
test.add_to_stack(3)
test.add_to_stack(54)
test.add_to_stack(312)
test.add_to_stack(212)
test.add_to_stack(212)
test.add_to_stack(212)
test.remove_from_stack()
test.remove_from_stack()
print(test.tab)
print(test.find_element(2))
