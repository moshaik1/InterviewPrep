
class LLNode:
    def __init__(self, value=None , nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    
    def addNode(self, value):
        # check if linked list is empty
        # if empty, make node the head and tail
        # update the next pointer to point to None
        node = LLNode(value)

        if self.head is None:
            self.head = node
            return
        
        
        curr = self.head
        while True:
            if curr.nextNode is None:
                curr.nextNode = node
                break
            curr = curr.nextNode

    
    def printLinkedList(self):
        currentNode = self.head

        while currentNode is not None:
            print (currentNode.value )
            print ("-->")
            print(currentNode.nextNode)
            currentNode = currentNode.nextNode
        print("None") 
                




        # if LinkedList not empty, make the node the tail
        # update the next pointer to point to None





demoLL = LinkedList()
demoLL.printLinkedList()
demoLL.addNode(10)
demoLL.printLinkedList()
demoLL.addNode(100)
demoLL.printLinkedList()
