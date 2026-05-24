class HashTable:
    def __init__(self,size):
        self.size = size
        self.table= [[]for _ in range(size)]


    def hash_function(self,key):
        return key % self.size

    def insert(self,key):
        index=self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)
        
h=HashTable(10)
h.insert(40) 
h.insert(50)
h.insert(60)   
h.display()    