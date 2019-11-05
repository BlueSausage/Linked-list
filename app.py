class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self):
        self.first = None

    def __len__(self):
        return self.count()

    def __getitem__(self, key):
        if type(key) is int:
            return self.get_at(key)
        else:
            raise Exception("Invalid key!")

    def is_empty(self):
        if self.first is None:
            return True
        return False

    def append(self, data):
        if self.is_empty():
            self.first = Node(data)
        else:
            currentNode = self.first
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = Node(data)

    def prepend(self, data):
        if self.is_empty():
            self.append(data)
        else:
            temp = self.first
            self.first = Node(data)
            self.first.nextNode = temp

    def remove_first(self):
        if self.is_empty():
            print("No Items in the List")
        if self.first.nextNode is None:
            self.first = None
        else:
            newFirstNode = self.first.nextNode
            self.first = None
            self.first = newFirstNode

    def remove_last(self):
        if self.is_empty():
            print("No Items in the List")
        elif self.first.nextNode is None:
            self.first = None
        else:
            lastNode = self.first
            while lastNode.nextNode.nextNode is not None:
                lastNode = lastNode.nextNode
            lastNode.nextNode = None

    def delete_at(self, index):
        if self.is_empty():
            print("Empty list")
            return False
        if index > self.count()-1 or index < 0:
            print("Error index invalid.")
            return False
        if index == 0:
            self.remove_first()
        currentNode = self.first
        for i in range(index):
            if i == index-1:
                temp = currentNode.nextNode.nextNode
                currentNode.nextNode = None
                currentNode.nextNode = temp
                break
            currentNode = currentNode.nextNode

    def clear_list(self):
        if self.is_empty():
            return "Empty list"
        currentNode = self.first
        while self.first.nextNode is not None:
            currentNode = self.first
            while currentNode.nextNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = None
        self.first = None

    def get_at(self, index):
        if self.is_empty():
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

    def get_index(self, nodeData):
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
        if self.is_empty():
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
    list.append("Erster Eintrag")
    list.append("Zweiter Eintrag")
    list.append("Dritter Eintrag")
    list.append("Vierter Eintrag")
    list.append("Fünfter Eintrag")
    list.print()
    print("-------")
