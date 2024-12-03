"""
Come fatto nell'esercizio precedente crea una classe
ma stavolta implementa la struttura dati Stack.
La classe, oltre i metodi/attributi dell'esercizio precedente,
deve prevedere altri tre metodi:
- peek: mostra l'elemento in cima allo stack
- is_empty: restituisce vero se lo stack è vuoto
- size: restituisce il numero degli elementi dello stack
"""
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, to_push):
        self.stack.append(to_push)

    def pop(self):
        self.stack.pop()

    def peek(self):
        print(self.stack[-1])

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True
        
    def size(self):
        return self.stack.__len__()

stack1 = Stack()
stack1.push(10)
stack1.push(11)
stack1.push(2)
stack1.push(60)
stack1.push(57)
print(stack1.size())
stack1.pop()
stack1.pop()
stack1.push(23)
stack1.peek()
print(stack1.is_empty())
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1.is_empty())
