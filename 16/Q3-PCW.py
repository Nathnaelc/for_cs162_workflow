class MyCollection:
    '''A custom collection class to demonstrate dunder methods.'''

    def __init__(self, elements):
        '''Initialize the collection with a list of elements.'''
        self.elements = elements

    def __len__(self):
        '''Return the length of the collection.'''
        return len(self.elements)

    def __getitem__(self, index):
        '''Retrieve an element from the collection by index.'''
        return self.elements[index]

    def __setitem__(self, index, value):
        '''Set the value of an element at a specific index.'''
        self.elements[index] = value

    def __delitem__(self, index):
        '''Delete an element at a specific index.'''
        del self.elements[index]

    def __contains__(self, value):
        '''Check if the collection contains a specific value.'''
        return value in self.elements

    def __str__(self):
        '''Return a string representation of the collection.'''
        return str(self.elements)

    def __eq__(self, other):
        '''Check if two collections are equal.'''
        if isinstance(other, MyCollection):
            return self.elements == other.elements
        return False


# Initialize the collection
my_collection = MyCollection([1, 2, 3, 4, 5])

# Show off the dunder methods
print(len(my_collection))  # Output should be 5
print(my_collection[2])  # Output should be 3
my_collection[2] = 10  # Set the value at index 2 to 10
print(my_collection[2])  # Output should be 10
del my_collection[2]  # Delete the element at index 2
print(10 in my_collection)  # Output should be False
print(my_collection)  # Output should be [1, 2, 4, 5]
print(my_collection == MyCollection([1, 2, 4, 5]))  # Output should be True

# Show off the documentation
help(MyCollection)
