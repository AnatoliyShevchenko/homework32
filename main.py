class Node:
    def __init__(self, data) -> None:
        self.item = data
        self.next = None
        self.prev = None
        self.start = None

    def __str__(self) -> str:
        return f'{self.prev} <-- [{self.item}] --> {self.next}'

    def insert_start(self, data):
        n = self
        new = Node(data)
        new.next = n.start
        n.prev = new
        n.start = new

    def delete_start(self):
        n = self
        n.prev = None

    def insert_end(self, data):
        n = self
        while n.next:
            n = n.next
        n.next = Node(data)

    def delete_end(self):
        n = self
        while n.next:
            n = n.next
        last_point = n
        n = self
        while n.next:
            if n.next == last_point:
                n.next = None
                break
            n = n.next


my_list = Node(1)
my_list.insert_start(0)
my_list.insert_start(5)
my_list.insert_end(2)
my_list.insert_end(4)
# my_list.delete_start()
# my_list.delete_end()
# my_list.delete_end()
print(my_list)