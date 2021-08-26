"""
    1) It needs to be consistent
    2) Every different word should map a different numbers
"""


class PhoneBook:
    def __init__(self):
        self.MAX = 100
        self.arr = [ None for i in range(self.MAX)]


    def get_hash(self, string):
        hash_val = 0
        for char in string:
            hash_val += ord(char)

        return hash_val % self.MAX


    def add_number(self, name, number):
        hash_val = self.get_hash(name)
        self.arr[hash_val] = number

    def get_number(self, name):
        hash_val = self.get_hash(name)
        return self.arr[hash_val]





if __name__=="__main__":
    phonebook = PhoneBook()

    phonebook.add_number("Avinash", 1234567890)
    phonebook.add_number("Lucifer", 5559997773)

    lucifer = phonebook.get_number("Lucifer")
    print(lucifer)
