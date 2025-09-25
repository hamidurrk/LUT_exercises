class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

    def append(self, data: object):
        new_node = Node(data, self.tail)

        curr_node = self.head
        for _ in range(self.len):
            curr_node = curr_node.next

        curr_node.next = new_node

        self.len += 1

    def insert(self, data: object, i: int):
        new_node = Node(data, None)

        curr_node = self.head
        for _ in range(i):
            curr_node = curr_node.next
        
        new_node.next = curr_node.next
        curr_node.next = new_node

        self.len += 1

    def delete(self, i: int):
        if i >= self.len:
            return None
        
        curr_node = self.head

        for _ in range(i):
            curr_node = curr_node.next
        
        deleting_value = curr_node.next.value
        curr_node.next = curr_node.next.next
        self.len -= 1
        return deleting_value        

    def index(self, data: object):
        idx = 0
        curr_node = self.head

        for _ in range(self.len):
            curr_node = curr_node.next
            if data == curr_node.value:
                return idx
            idx += 1
        return -1
    
    def swap(self, i: int, j: int):
        i_value = self.get_value(i)
        j_value = self.get_value(j)

        self.delete(i)
        self.insert(j_value, i)
        self.delete(j)
        self.insert(i_value, j)

    def get_value(self, idx: int):
        curr_node = self.head

        for i in range(self.len):
            curr_node = curr_node.next
            if i == idx:
                return curr_node.value
        return None

    def print(self):
        curr_node = self.head

        for i in range(self.len):
            curr_node = curr_node.next
            print(curr_node.value, end="")
            
            if i != self.len-1:
                print(" -> ", end="")
            else:
                print()

if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()
    print(L.index(7))   
    print(L.index(9))      
    L.swap(1, 4)
    L.print()
    L.swap(2, 0)
    L.print()
