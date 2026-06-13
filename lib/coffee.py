#!/usr/bin/env python3
class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Note: Using the exact apostrophe from the test (curly apostrophe)
        print("This coffee is great, here’s a tip!")
        self.price += 1