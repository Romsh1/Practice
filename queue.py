class Queue:
    def __init__(self):
        self.__items = []
        self.front = 0

    #O(1)* or constant time --> adding to the end of list
    def enqueue(self, e):
        self.__items.append(e)

    #O(1)* or constant time --> removing first item of list
    def dequeue(self):
        item = self.__items[self.front] #Gets item at front of queue
        self.__items[self.front] = None
        self.front += 1
        return item
    
    #O[1]
    def first(self):
        return self.__items[self.front]
    
    #O[1]
    def __len__(self):
        return len(self.__items) - self.front
    
    #O[1]
    def is_empty(self):
        return len(self) == 0 
    
#main
q1 = Queue()    #[]
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3) #[1,2,3] --> f=0
print(len(q1)) #3

print(q1.dequeue()) #return 1 --> [None, 2, 3] f = 1
print(len(q1)) #2
