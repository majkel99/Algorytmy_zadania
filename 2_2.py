class PriorityQueue:
    def __init__(self):
        self.max = 5
        self.tab = [] * self.max
        self.length = 0
    def add_to_q(self, obj, prt):
        if isinstance(prt, int):
            i=0
            inserted = False
            if self.max>self.length:
                try:
                    while not inserted:
                        if self.tab[i][1]<prt:
                            self.tab=self.tab[:i]+[(obj,prt)]+self.tab[i:]
                            self.length+=1
                            inserted=True
                        i+=1
                except IndexError:
                    self.tab+=[(obj,prt)]
                    self.length+=1
            else:
                print("Tablica jest pełna!")
        else:
            print("Priorytet musi być zmienną typu int")

    def remove_from_q(self):
        if self.length == 0:
            raise IndexError("Queue is empty")
        result = self.tab[0]
        self.tab=self.tab[1:]
        self.length -= 1
        return result

    def find_element(self, element):
        try:
            return self.tab[element]
        except Exception as e:
            return e


test=PriorityQueue()
test.add_to_q("e", "2")
test.add_to_q(2, "3")
test.add_to_q("ef", 4)
test.add_to_q(5, 6)
test.add_to_q(5, 9)
test.add_to_q(5, 4)
print(test.tab)
print(test.find_element(2))
test.remove_from_q()
print(test.tab)

