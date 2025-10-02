class HashBucket:
    def __init__(self, M: int, B: int):
        self.size = M
        self.buckets = B
        self.bucket_size = M // B
        self.table = [None] * M
        self.overflow = []
    
    def hash(self, data: str) -> int:
        ascii_sum = 0
        for char in data:
            ascii_sum += ord(char)
        return ascii_sum % self.buckets
    
    def print(self):
        result = []
        for item in self.table:
            if item is None:
                result.append('F') 
            elif item == "TOMBSTONE":
                result.append('T')  
            else:
                result.append(item)  

        for item in self.overflow:
            if item == "TOMBSTONE":
                result.append('T')
            else:
                result.append(item)
        
        print(' '.join(result))
    
    def insert(self, data: str):
        bucket = self.hash(data)
        start_pos = bucket * self.bucket_size
        end_pos = start_pos + self.bucket_size
        
        for i in range(start_pos, end_pos):
            if self.table[i] == data:
                return
        
        for item in self.overflow:
            if item == data:
                return
        
        first_tombstone = None
        for i in range(start_pos, end_pos):
            if self.table[i] is None:
                if first_tombstone is not None:
                    self.table[first_tombstone] = data
                else:
                    self.table[i] = data
                return
            if self.table[i] == "TOMBSTONE" and first_tombstone is None:
                first_tombstone = i
        
        if first_tombstone is not None:
            self.table[first_tombstone] = data
            return
        
        self.overflow.append(data)
    
    def delete(self, data: str):
        for i in range(self.size):
            if self.table[i] == data:
                self.table[i] = "TOMBSTONE"
                return
        
        for i, value in enumerate(self.overflow):
            if value == data:
                del self.overflow[i]
                return


if __name__ == "__main__":
    table = HashBucket(8, 4)
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