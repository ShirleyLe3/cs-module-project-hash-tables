class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HashTableEntry({self.key}, {self.value})"
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        return self.capacity

    def get_load_factor(self):
        return self.count / self.capacity

    def fnv1(self, key):
        encoded_key = key.encode()
        offset_basis = 14695981039346656037
        fnv_prime = 1099511628211

        hash_key = offset_basis  # 64-bit offset_basis
        for byte in encoded_key:
            hash_key = hash_key * fnv_prime
            hash_key = hash_key ^ byte

        return hash_key

    def djb2(self, key):
        pass

    def hash_index(self, key):
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        if self.storage[self.hash_index(key)] is None:
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)
            self.count += 1
        else:
            current = self.storage[self.hash_index(key)]
            while True:
                if current.key == key:
                    current.value = value
                    break
                elif current.next is not None:
                    current = current.next
                else:
                    current.next = HashTableEntry(key, value)
                    self.count += 1
                    break
        #TODO if overloaded, resize

    def delete(self, key):
        # TODO traverse linked-list to remove item
        if self.storage[self.hash_index(key)]:
            self.storage[self.hash_index(key)] = None
        else:
            print("Value not found.")

    def get(self, key):
        # TODO traverse linked-list to get item
        if self.storage[self.hash_index(key)]:
            return self.storage[self.hash_index(key)].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
