class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def infix_postfix(infix_expression):
    operators= {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}
    oper_stack = Stack() # stos operatorow
    result = [] # Wyjscie

    for i in infix_expression:
        if i.isalnum():
            result.append(i)
        elif i == "(":
            oper_stack.push(i)
        elif i == ")":
            while oper_stack.peek() != "(":
                result.append(oper_stack.pop())
            oper_stack.pop() # zrzucenie "(" ze stosu
        else:
            while not oper_stack.isEmpty() and operators[oper_stack.peek()] >= operators[i]:
                result.append(oper_stack.pop())
            oper_stack.push(i)

    while not oper_stack.isEmpty():
        result.append(oper_stack.pop())

    return "".join(result)

expression="4*(5-6/3+1)^2"
print("Konwersja z notacji infiksowej", expression ,"na postać postfiksową:", infix_postfix(expression))

def postfix_infix(postfix_expression):
    stack = Stack()
    for i in postfix_expression:
        if i in "+-*/^":
            last_num=stack.pop()
            stack.push("("+stack.pop()+i+last_num+")")
        else:
            stack.push(i)
    return stack.peek()

print("Konwersja z notacji postfiksowej", infix_postfix(expression) ,"na postać infiksową:",postfix_infix(infix_postfix(expression)))


