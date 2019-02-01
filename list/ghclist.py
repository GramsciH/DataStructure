class GHCList:
    def __init__(self):
        self.elem = None

    def __getitem__(self, key):
        if key >= self.length() or key < 0:
            raise IndexError('list index out of range')

        if key == 0:
            result = self.elem
        else:
            result = self.next[key - 1]
        return result

    def empty(self):
        return self.elem is None

    def add(self, elem):
        if self.elem is None:
            self.elem = elem
            self.next = GHCList()
        else:
            self.next.add(elem)

    def remove(self, index):
        if index >= self.length() or index < 0:
            raise IndexError('list index out of range')

        if self.empty():
            result = None
        else:
            if index == 0:
                result = self.elem
                self.elem = self.next.elem
                self.next = self.next.next
            else:
                result = self.next.remove(index - 1)
        return result

    def get_first_elem(self):
        return self.elem

    def length(self):
        if self.empty():
            result = 0
        else:
            result = 1 + self.next.length()

        return result

# ghc_list = GHCList()
# ghc_list.add(1)
# ghc_list.add(3)
# ghc_list.add(4)
# print(ghc_list.length()==3)
# ghc_list.remove(0)
# print(ghc_list.length()==2)
