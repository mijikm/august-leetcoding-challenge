# Approach 1: Key as index
# Time Complexity: O(1)
# Space Complexity: O(1)

#class MyHashSet(object):

#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.data = [-1] * 1000001

#    def add(self, key):
#        """
#        :type key: int
#        :rtype: None
#        """
#        if self.data[key] == -1:
#            self.data[key] = 1

#    def remove(self, key):
#        """
#        :type key: int
#        :rtype: None
#        """
#        self.data[key] = -1

#    def contains(self, key):
#        """
#        Returns true if this set contains the specified element
#        :type key: int
#        :rtype: bool
#        """
#       return self.data[key] == 1

# Approach 2: Hashing
# Time Complexity: O(1)
# look up time for hash set is O(1)
# Space Complexity: O(1)
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculate_hash_value(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculate_hash_value(key)
        if self.table[hv] != None:
            # e.g. [1,2,3,2] remove all 2s needs while loop
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hv = self.calculate_hash_value(key)
        if self.table[hv] != None:
            return key in self.table[hv]
        return False


if __name__ == '__main__':
    obj = MyHashSet()
    print(obj.contains(1)) # False
    obj.add(1)
    obj.add(2)
    print(obj.contains(2)) # True
    print(obj.contains(3)) # False
    obj.add(1)
    obj.add(3)
    obj.add(2)
    print(obj.contains(3)) # True
    obj.add(2)
    obj.add(2)
    obj.add(2)
    print(obj.contains(2)) # True
    obj.remove(2)
    print(obj.contains(2)) # False


