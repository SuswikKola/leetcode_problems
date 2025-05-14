class MyHashMap:

    def __init__(self):
        self.dict_a = {}
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict_a:
            self.dict_a[key] = value
        else:
            self.dict_a[key]= value
        

    def get(self, key: int) -> int:
        if key in self.dict_a:
            return self.dict_a[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.dict_a:
            del self.dict_a[key]

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)