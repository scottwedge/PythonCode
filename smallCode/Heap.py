#!/usr/bin/env python

class Heap(object):
    """docstring for Heap"""
    def __init__(self, args=None):
        super(Heap, self).__init__()
        self.arg = []
        if args != None:
            self.build_heap(args)

    def build_heap(self, arg):
        """start building the heap"""
        for item in arg:
            self.insert(item)

    """
initial state: []

after inserg 5: [5]

after insert 12:  [12, 5]

                     [12]
                    / 
                  [5]

after insert 3: [12, 5, 3]

                     [12]
                    /   \
                  [5]    [3]

after insert 7: [12, 7, 3, 5]

                       [12]
                      /   \
                    [7]    [3]
                   /
                [5]

after insert 33:  [33, 12, 3, 5, 7]

                       [33]
                      /    \
                   [12]     [3]
                   /  \
                [5]    [7]

    """
    def insert(self, elem):
        self.arg.append(elem)
        cur = len(self.arg) - 1

        par = (cur - 1) / 2
        while cur > 0 and elem > self.arg[par]:
            self.arg[cur] = self.arg[par]
            cur = par
            par = (cur - 1) / 2
        self.arg[cur] = elem
        #print "current state: ", self.arg
    """
The pop function select the first element from the heap each time, 
or None if the heap is empty. After select the element, restructure
the heap by moving the bigger child element to their parent.
    """
    def pop(self):
        size = len(self.arg)
        if size <= 0:
            return None
        else:
            elem = self.arg[0]
            cur = 0
            while 2 * cur + 1 < size:
                l = 2 * cur + 1
                r = 2 * cur + 2
                if r < size and self.arg[l] < self.arg[r]:
                    l = r
                if self.arg[size-1] >= self.arg[l]:
                    break
                else:
                    self.arg[cur] = self.arg[l]
                    cur = l

            self.arg[cur] = self.arg[size - 1]
            self.arg = self.arg[:size-1]
            return elem

    def top(self):
        """Get the value of the top element"""
        if len(self.arg) == 0:
            return None
        else:
            return self.arg[0]

if __name__ == '__main__':
    nums = []
    size = int(raw_input('Please input the size: '))
    for i in range(0, size):
        nums.append(int(raw_input('The ' + str(i) + 'th number: ')))
    print "Your input: ", nums

    h = Heap(nums)
    #for item in nums:
    #    h.insert(item)

    while h.top() != None:
        print h.pop()
