class SortedList:

    def __init__(self):
        self.sorted_list = []
        self.length = 0

    def print_list(self):
        print(self.sorted_list)

    def get_length(self):
        return self.length

    def head(self):
        if self.length > 0:
            return self.sorted_list[0]
        else:
            return None

    def tail(self):
        if self.length > 0:
            return self.sorted_list[self.length - 1]
        else:
            return None

    def insert(self, node):
        self.sorted_list.append(node)
        self.sorted_list.sort()
        self.length += 1
        return self.sorted_list.index(node)

    def pop_smallest(self):
        if self.length == 0:
            return None

        else:
            smallest = self.sorted_list[0]
            self.sorted_list.remove(smallest)
            self.length -= 1
            return smallest

    def pop_highest(self):
        if self.length == 0:
            return None

        else:
            highest = self.sorted_list[self.length - 1]
            self.sorted_list.remove(highest)
            self.length -= 1
            return highest

    def is_empty(self):
        return self.length == 0
