class TimeMap:
    # Stores key:key and value:tuples (key, value, timestamp)
    objs = {}

    def __init__(self):
        self.objs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.objs:
            # Insertion sort
            i = len(self.objs[key])
            while i > 0 and self.objs[key][i - 1][2] > timestamp:
                i -= 1

            if i == len(self.objs[key]):
                self.objs[key].append((key, value, timestamp))
            else:
                self.objs[key].insert(i, (key, value, timestamp))
        else:
            self.objs[key] = [(key, value, timestamp)]
        # print(self.objs)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.objs:
            for i in range(len(self.objs[key]) - 1, -1, -1):
                obj = self.objs[key][i]

                if obj[0] == key and obj[2] <= timestamp:
                    return obj[1]
            # If timestamp (and those lesser than specified) not found
            return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 1))  # bar
    print(obj.get("foo", 3))  # bar
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))  # bar2
    print(obj.get("foo", 5))  # bar2
    obj.set("foo", "bar3", 6)
    print(obj.get("foo", 6))  # bar3
    print(obj.get("foo", 7))  # bar3
    obj.set("foo", "bar4", 8)
    print(obj.get("foo", 8))  # bar4
    print(obj.get("foo", 9))  # bar4
    obj.set("foo", "bar5", 10)
    print(obj.get("foo", 10))  # bar5
    print(obj.get("foo", 11))  # bar5
    obj.set("foo", "bar6", 12)
    print(obj.get("foo", 12))  # bar6
    print(obj.get("foo", 13))  # bar6
    obj.set("foo", "bar7", 14)
    print(obj.get("foo", 14))  # bar7
    print(obj.get("foo", 15))  # bar7
    obj.set("foo", "bar8", 16)
    print(obj.get("foo", 16))  # bar8
    print(obj.get("foo", 17))  # bar8
    obj.set("foo", "bar9", 18)
    print(obj.get("foo", 18))  # bar9
    print(obj.get("foo", 19))  # bar9
    obj.set("foo", "bar10", 20)
    print(obj.get("foo", 20))  # bar10
    print(obj.get("foo", 21))  # bar10
    obj.set("foo", "bar11", 22)
    print(obj.get("foo", 22))  # bar11
    print(obj.get("foo", 23))  # bar11
