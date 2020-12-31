
from node import Node

class singlylinkedlist:

    def __init__(self):
          
      self.head=None
    
#put some comments for practice purpose    
      
    def addnode(self,value):
        newnode=Node(value)
        if self.head is None:
              self.head=newnode
              print("new node added")
              print(self.head.value)
              return(self.head)
      
        elif self.head is not None:
              self.head.next=newnode
              print("new node added")
              print(self.head.next.value)
              return(self.head.next)
              
        
    def printlst(self):
          
        if self.head is not None:
              print(self.head.value)
              while True:
                self.head=self.head.next
                print(self.head.value)
                if self.head.next is None:
                      break
              
              
             
        
        
class Doublylinkedlist:
    pass
        
   

#tests

ssl1=singlylinkedlist()
n1=ssl1.addnode(5)
n2=ssl1.addnode(50)
n3=ssl1.addnode(555)


n1.next=n2
n2.next=n3

print("printed singly link list\n")
ssl1.printlst()
          
        
    
