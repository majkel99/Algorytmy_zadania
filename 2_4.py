class List:
    def __init__(self):
        self.max=5
        self.tab=[None]*self.max
        self.length=0
    def add_to_list(self, obj, ind):
        try:
            if isinstance(ind, int):
                if self.max > self.length:
                    if self.tab[ind]==None:
                        self.tab[ind]=obj
                        self.length+=1
                    else:
                        print("Obiekt o takim indeksie znajduje się już w tablicy")
                else:
                    print("Lista jest pełna")
            else:
                print("Indeks musi być zmienną typu int")
        except Exception as e:
            print("Niepoprawny indeks")
    def remove_from_list(self, ind):
        try:
            if isinstance(ind, int):
                if self.length!=0 and self.tab[ind]!=None:
                    temp=self.tab[ind]
                    self.tab[ind]=None
                    self.length-=1
                    return temp
                elif self.tab[ind]==None:
                    print("Lista w podanym indeksie jest pusta!")
                else:
                    print("Lista jest pusta")
            else:
                print("Indeks musi być zmienną typu int")
        except IndexError as e:
            print(e)
    def find_element(self, ind):
        try:
            if isinstance(ind, int):
                    return self.tab[ind]
            else:
                print("Indeks musi być zmienną typu int")
        except IndexError as e:
            print(e)
    def wypisz_elementy(self):
        return self.tab
lista=List()
lista.add_to_list(5,4)
lista.add_to_list(5,3)
lista.add_to_list(3,2)
lista.add_to_list(4,1)
lista.add_to_list(4,"f")
lista.add_to_list("e",0)
print(lista.wypisz_elementy())
lista.remove_from_list(4)
lista.remove_from_list(4)
lista.remove_from_list(2)
lista.add_to_list(4,0)
lista.add_to_list(321,2)
print(lista.wypisz_elementy())
print(lista.find_element(4))
print(lista.find_element(5))
print(lista.find_element(3))
print(lista.find_element(2))
print(lista.find_element(1))
print(lista.find_element(0))


