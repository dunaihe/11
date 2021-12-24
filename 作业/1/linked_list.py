class Node(object):
    current_node = None

    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, n):
        self._next = n
    def __iter__(self):
        self.now_node = self
        return self
    def __next__(self):
        res = self.now_node
        if res is None:
            raise StopIteration
        else:
            self.now_node = self.now_node.next
            return res

def flatten(n):
    r = []
    for i in n:
        if isinstance(i.value, Node):
            r = r + flatten(i.value)
        else:
            r.append(i.value)
    return r


r1 = Node(1)  
r2 = Node(7, Node(2, Node(9)))  
r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
flat_r3 = flatten(r3) 


r3_expected = [3, 19, 25, 12]
assert r3_expected == list(flat_r3)
