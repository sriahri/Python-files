class HashTable:
    # Please implement each of the following methods following the guide.
    # Here, I've only implemented the construction methods and the dunder __repr__ method. Do not change them.

    class Node:

        def __init__(self, key, value, next=None):
            # Inside each node, there are three attributes
            # 1. self.key stores a string as the key
            # 2. self.value stores a string as value
            # 3. self.next is a pointer that points to the next node

            #################### DO NOT CHANGE ####################
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, n=1000):
        # A new HashTable contains an array of size n containing only None objects.
        # A new HashTable also contains a list (empty initially) to store all the keys stored in the HashTable.
        # Note that, self.keys is a list, you may use methods implemented for list objects.

        #################### DO NOT CHANGE ####################
        self.table = [None] * n
        self.keys = []

    def __len__(self):
        return len(self.table)
        # This method implements "len(HashTable)".
        # return the number of keys stored in the HashTable.

    def __setitem__(self, key, value):
        index = hash(key) % len(self.table)
        self.table[index] = HashTable.Node(key, value)
        if key is None:
            self.table[index]
            self.key.appen(key)
        else:
            self.table
        # This method implements "HashTable[key] = value"
        # Use hash(key) % len(self.table) as the index for the key-value pair.
        # Wrap the key-value pair into a node.
        # If key is new, store this node into the LinkedList (could be empty) stored in self.table[index].
        # Note that, the node does not have to be linked to the tail of that list.
        # Remind that, if the key is new, you also need to append the key to self.keys.
        # If key is not new, update the old corresponding value to the new one.

    def __getitem__(self, key):
        if key in self.keys:
            self.table[key]
        # self.table[index]
        else:
            raise KeyError(key)
        # This method implements "HashTable[key]"
        # If key is in the HashTable, return the corresponding value of key.
        # Remind that, if key exists, it can only appear in self.table with index = hash(key) % len(self.table).
        # If key is not in the HashTable, raise KeyError(key).

    def __contains__(self, key):
        if key in self.keys:
            return True
        else:
            return False
        # This method implements "key in HashTable"
        # Return a boolean that represents whether key is in the HashTable.
        # Note that, DO NOT use "key in self.keys", because it needs O(n) time.
        # This operation is expected to have a constant running time.

    def __iter__(self):
        for key in self.keys:
            yield self.keys.key
        # This method implements "for key in HashTable"
        # Yield each key in self.keys

    def __repr__(self):
        # This method implements "print(HashTable)"

        #################### DO NOT CHANGE THIS ####################
        return "{" + ','.join(repr(key) + ':' + repr(self[key]) for key in self) + "}"


########################################################################################################################
###################################### ############################################
###################################### DO NOT CHANGE ANYTHING BELOW ############################################
###################################### ############################################
########################################################################################################################
print("Let's create a HashTable to store letters in the phonetic alphabet.")

ht1 = HashTable(10)
ht1["a"] = "Alfa"
ht1["b"] = "Bravo"
ht1["c"] = "Charlie"
print("We start with a HashTable with only 10 spots and then store the first three letters, "
      "ht1 =", ht1, ".")
print(ht1.__repr__())
print("In the phonetic alphabet, \'c\' is for", ht1["c"], ".")

ht1["a"] = "Alpha"
print("We change the spelling of word \'Alfa\' to \'Alpha\', then ht1 =", ht1, ".")

print("Does ht1 contain letter \'d\'? The answer is", "d" in ht1, ".")
ht1["d"] = "Delta"
ht1["e"] = "Echo"
ht1["f"] = "Foxtrot"
ht1["g"] = "Golf"
ht1["h"] = "Hotel"
ht1["i"] = "India"
ht1["j"] = "Juliett"
ht1["k"] = "Kilo"
print("To test whether collisions are handled correctly, "
      "we keep inserting eight more letters; and now there are", len(ht1), "letters in ht1.")
print("By pigeonhole principle, a collision is guaranteed.")
print("Now, ht1 becomes", ht1, ".")
