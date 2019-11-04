class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

class List:
    def __init__(self):
        self.first = None

    def isEmpty(self):
        if self.first is None:
            return True
        return False

    def append(self, data):
        if self.isEmpty():
            self.first = Node(data)
        else:
            currentNode = self.first
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = Node(data)

    def prepend(self, data):
        if self.isEmpty():
            self.append(data)
        else:
            temp = self.first
            self.first = Node(data)
            self.first.nextNode = temp

    def removeFirst(self):
        if self.isEmpty():
            print("No Items in the List")
        if self.first.nextNode is None:
            self.first = None
        else:
            newFirstNode = self.first.nextNode
            self.first = None
            self.first = newFirstNode

    def removeLast(self):
        if self.isEmpty():
            print("No Items in the List")
        elif self.first.nextNode is None:
            self.first = None
        else:
            lastNode = self.first
            while lastNode.nextNode.nextNode is not None:
                lastNode = lastNode.nextNode
            lastNode.nextNode = None         

    def deleteAt(self, index):
        if self.isEmpty():
            return "Empty list"
        if index > self.count()-1 or index < 0:
            return "Error index invalid."
        else:
            currentNode = self.first
            size = self.count()
            for i in range(size):
                if i == index:
                    print(currentNode)
                currentNode = currentNode.nextNode

    def getAt(self, index):
        if self.isEmpty():
            return "Empty list"
        if index > self.count()-1 or index < 0:
            return "Error index invalid."
        else:
            currentNode = self.first
            size = self.count()
            for i in range(size):
                if i == index:
                    return currentNode
                currentNode = currentNode.nextNode

    def getIndex(self, nodeData):
        if not nodeData:
            return "Data is empty"
        else:
            if self.first is not None:
                index = 0
                currentNode = self.first
                while currentNode is not None:
                    if currentNode.data is nodeData:
                        return index
                    index += 1
                    currentNode = currentNode.nextNode
                return -1
            else:
                return "List is empty"

    def count(self):
        count = 0
        currentNode = self.first
        if currentNode is not None:
            while currentNode is not None:
                count += 1
                currentNode = currentNode.nextNode
        return count

    def print(self):
        if self.isEmpty():
            print("No items in the list")
        elif self.first.nextNode is None:
            print(self.first)
        else:
            currentNode = self.first
            while currentNode is not None:
                print(currentNode)
                currentNode = currentNode.nextNode

if __name__ == '__main__':
    list = List()
    print(list.count())
    print("-------")
    list.append("Erster Eintrag")
    list.append("Zweiter Eintrag")
    list.append("Dritter Eintrag")
    list.append("Vierter Eintrag")
    list.append("Fünfter Eintrag")
    list.print()
    print("-------")
    print("Count: " + str(list.count()))
    print("-------")
    list.prepend("Nullter Eintrag")
    list.print()
    print("-------")
    print("Count: " + str(list.count()))
    print("-------")
    print(list.getIndex("Dritter Eintrag"))
    print("-------")
    print(list.getAt(5))
    print("-------")
    list.removeLast()
    list.print()
    print("-------")
    list.removeFirst()
    list.print()
    print("-------")
    list.removeFirst()
    list.removeLast()
    list.print()
    print("-------")
    list.prepend("Erster Eintrag")
    list.append("Vierter Eintrag")
    list.print()
    print("-------")
    list.deleteAt(0)