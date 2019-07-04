from hashtable import HashTable
from linkedlist import LinkedList, Node

class Set(HashTable):

    def __init__(self, init_size=8, elements=None):
        super(Set, self).__init__(init_size)
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        """Check if the given element is in the set, return a boolean indicating if the
        element was found or not
        Time Complexity: O(1)"""
        return super(Set, self).contains(element)


    def add(self, element):
        """Check to see if the given element does not exist in the Set
        if it doesn't add the given element to the set
        Time Complexity: Avg O(1) Worst O(n)"""
        if self.contains(element) == False:
            self.set(element, None)


    def remove(self, element):
        """Remove the given element from the set
        Time Complexity: O(1)"""
        self.delete(element)

    def union(self, other_set):
        """Combine 2 sets into a new set, return the new set
        Time Complexity: O(n * m)"""
        new_set = Set()

        for item in self.keys():
            new_set.add(item)

        for item in other_set.keys():
            new_set.add(item)

        return new_set

    def difference(self, other_set):
        """Take the unique elements from both sets and return them in a new set
        Time Complexity: O(n)"""
        new_set = Set()

        for item in self.keys():
            if not other_set.contains(item):
                new_set.add(item)

        return new_set

    def intersection(self, other_set):
        """Take the elements that are shared by both sets and return them in a new set
        Time Complexity: O(n)"""
        new_set = Set()

        for item in self.keys():
            if other_set.contains(item):
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        """Checks to see if every element in this set is also into the other set
        Time Complexity: O(n)"""

        for item in self.keys():
            if not other_set.contains(item):
                return False

        return True


set = Set()
set.add('A')
set.add('B')
set.add('C')
set.add('F')

set2 = Set()
set2.add('B')
set2.add('E')
set2.add('F')
set2.add('G')

set3 = Set()
set3.add('B')
set3.add('Z')

print(set)
print(set2)

union_set = set.union(set2)
diff_set = set.difference(set2)
inter_set = set.intersection(set2)

print(union_set)
print(diff_set)
print(inter_set)
print(set3.is_subset(set))
