class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def appendToTail(self, data):
        end = Node(data)
        n = self

        while n.next != None:
            n = n.next
        n.next = end

    def getElement(self):
        n = self
        retval = []
        while True:
            if n.next == None:
                retval.append(n.data)
                break
            retval.append(n.data)
            n = n.next
        return retval

    def __str__(self):
        n = self
        retval = []
        while True:
            if n.next == None:
                retval.append(n.data)
                break
            retval.append(n.data)
            n = n.next
        return str(retval)

def deleteNode(node, data):
    if node.data == data:
        return node.next
    while node.next!= Node:
        if node.next.data == data:
            node.next = node.next.next
            return node
        node = node.next

    return node



node = Node(1)
node.appendToTail(3)
node.appendToTail(7)
node.appendToTail(8)
node.appendToTail(8)
node.appendToTail(8)
node.appendToTail(8)
node.appendToTail(8)
node.appendToTail(7)
node.appendToTail(7)
node.appendToTail(7)
node.appendToTail(7)
node.appendToTail(3)
node.appendToTail(2)
node.appendToTail(7)
node.appendToTail(10)

checkSet=set()
for data in node.getElement():
    if data not in checkSet:
        checkSet.add(data)
    else:
        deleteNode(node, data)

print(node.getElement())