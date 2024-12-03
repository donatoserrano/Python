"""
Crea una classe che implementa la struttura dati Queue.
Possiede un attributo che rappresenta la collezione,
e due metodi: enqueue e dequeue.
Istanzia quindi un oggetto della classe e testalo
per valutare se funziona come atteso.
"""
from collections import deque

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, to_enqueue):
        self.queue.append(to_enqueue)

    def dequeue(self):
        self.queue.popleft()

    def print_queue(self):
        for item in self.queue:
            print(item)

queue1 = QueueManager()
queue1.enqueue(10)
queue1.enqueue(112)
queue1.enqueue(9)
queue1.dequeue()
queue1.enqueue(72)
queue1.print_queue()