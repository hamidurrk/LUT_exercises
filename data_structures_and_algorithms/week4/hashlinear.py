class HashLinear:
    def __init__(self, M: int):
        self.size = M
        self.table = [None] * M
    
    def hash(self, data: str) -> int:
        ascii_sum = 0
        for char in data:
            ascii_sum += ord(char)
        return ascii_sum % self.size
    
    def print(self):
        result = []
        for item in self.table:
            if item is None:
                result.append('F')  
            elif item == "TOMBSTONE":
                result.append('T')  
            else:
                result.append(item)  
        print(' '.join(result))
    
    def insert(self, data: str):
        position = self.hash(data)
        
        first_tombstone = None
        start_pos = position
        
        while True:
            if self.table[position] == data:
                return
                
            if self.table[position] is None:
                if first_tombstone is not None:
                    self.table[first_tombstone] = data
                else:
                    self.table[position] = data
                return
                
            if self.table[position] == "TOMBSTONE" and first_tombstone is None:
                first_tombstone = position
            
            position = (position + 1) % self.size
            
            if position == start_pos:
                if first_tombstone is not None:
                    self.table[first_tombstone] = data
                return
    
    def delete(self, data: str):
        position = self.hash(data)
        start_pos = position
        while True:
            if self.table[position] == data:
                self.table[position] = "TOMBSTONE"
                return
                
            if self.table[position] is None:
                return
            
            position = (position + 1) % self.size
            
            if position == start_pos:
                return


if __name__ == "__main__":
    table = HashLinear(8)
    table.print()

    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()